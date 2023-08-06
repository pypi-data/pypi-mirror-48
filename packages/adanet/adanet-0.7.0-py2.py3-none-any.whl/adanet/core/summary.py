"""Tensorboard summaries for the single graph AdaNet implementation.

Copyright 2018 The AdaNet Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import contextlib
import os

from absl import logging
from adanet import tf_compat
import tensorflow as tf
# pylint: disable=g-direct-tensorflow-import
from tensorflow.python.ops import summary_op_util
from tensorflow.python.ops import summary_ops_v2 as summary_v2_lib
from tensorflow.python.summary import summary as summary_lib
# pylint: enable=g-direct-tensorflow-import

_DEFAULT_SCOPE = "default"


class Summary(object):
  """Interface for writing summaries to Tensorboard."""

  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def scalar(self, name, tensor, family=None):
    """Outputs a `tf.Summary` protocol buffer containing a single scalar value.

    The generated tf.Summary has a Tensor.proto containing the input Tensor.

    Args:
      name: A name for the generated node. Will also serve as the series name in
        TensorBoard.
      tensor: A real numeric Tensor containing a single value.
      family: Optional; if provided, used as the prefix of the summary tag name,
        which controls the tab name used for display on Tensorboard.

    Returns:
      A scalar `Tensor` of type `string`. Which contains a `tf.Summary`
      protobuf.

    Raises:
      ValueError: If tensor has the wrong shape or type.
    """

  @abc.abstractmethod
  def image(self, name, tensor, max_outputs=3, family=None):
    """Outputs a `tf.Summary` protocol buffer with images.

    The summary has up to `max_outputs` summary values containing images. The
    images are built from `tensor` which must be 4-D with shape `[batch_size,
    height, width, channels]` and where `channels` can be:

    *  1: `tensor` is interpreted as Grayscale.
    *  3: `tensor` is interpreted as RGB.
    *  4: `tensor` is interpreted as RGBA.

    The images have the same number of channels as the input tensor. For float
    input, the values are normalized one image at a time to fit in the range
    `[0, 255]`.  `uint8` values are unchanged.  The op uses two different
    normalization algorithms:

    *  If the input values are all positive, they are rescaled so the largest
    one is 255.
    *  If any input value is negative, the values are shifted so input value 0.0
      is at 127.  They are then rescaled so that either the smallest value is 0,
      or the largest one is 255.

    The `tag` in the outputted tf.Summary.Value protobufs is generated based on
    the
    name, with a suffix depending on the max_outputs setting:

    *  If `max_outputs` is 1, the summary value tag is '*name*/image'.
    *  If `max_outputs` is greater than 1, the summary value tags are
      generated sequentially as '*name*/image/0', '*name*/image/1', etc.

    Args:
      name: A name for the generated node. Will also serve as a series name in
        TensorBoard.
      tensor: A 4-D `uint8` or `float32` `Tensor` of shape `[batch_size, height,
        width, channels]` where `channels` is 1, 3, or 4.
      max_outputs: Max number of batch elements to generate images for.
      family: Optional; if provided, used as the prefix of the summary tag name,
        which controls the tab name used for display on Tensorboard.

    Returns:
      A scalar `Tensor` of type `string`. The serialized `tf.Summary` protocol
      buffer.
    """

  @abc.abstractmethod
  def histogram(self, name, values, family=None):
    """Outputs a `tf.Summary` protocol buffer with a histogram.

    Adding a histogram summary makes it possible to visualize your data's
    distribution in TensorBoard. You can see a detailed explanation of the
    TensorBoard histogram dashboard
    [here](https://www.tensorflow.org/get_started/tensorboard_histograms).

    The generated [`tf.Summary`](
    tensorflow/core/framework/summary.proto)
    has one summary value containing a histogram for `values`.

    This op reports an `InvalidArgument` error if any value is not finite.

    Args:
      name: A name for the generated node. Will also serve as a series name in
        TensorBoard.
      values: A real numeric `Tensor`. Any shape. Values to use to build the
        histogram.
      family: Optional; if provided, used as the prefix of the summary tag name,
        which controls the tab name used for display on Tensorboard.

    Returns:
      A scalar `Tensor` of type `string`. The serialized `tf.Summary` protocol
      buffer.
    """

  @abc.abstractmethod
  def audio(self, name, tensor, sample_rate, max_outputs=3, family=None):
    """Outputs a `tf.Summary` protocol buffer with audio.

    The summary has up to `max_outputs` summary values containing audio. The
    audio is built from `tensor` which must be 3-D with shape `[batch_size,
    frames, channels]` or 2-D with shape `[batch_size, frames]`. The values are
    assumed to be in the range of `[-1.0, 1.0]` with a sample rate of
    `sample_rate`.

    The `tag` in the outputted tf.Summary.Value protobufs is generated based on
    the
    name, with a suffix depending on the max_outputs setting:

    *  If `max_outputs` is 1, the summary value tag is '*name*/audio'.
    *  If `max_outputs` is greater than 1, the summary value tags are
      generated sequentially as '*name*/audio/0', '*name*/audio/1', etc

    Args:
      name: A name for the generated node. Will also serve as a series name in
        TensorBoard.
      tensor: A 3-D `float32` `Tensor` of shape `[batch_size, frames, channels]`
        or a 2-D `float32` `Tensor` of shape `[batch_size, frames]`.
      sample_rate: A Scalar `float32` `Tensor` indicating the sample rate of the
        signal in hertz.
      max_outputs: Max number of batch elements to generate audio for.
      family: Optional; if provided, used as the prefix of the summary tag name,
        which controls the tab name used for display on Tensorboard.

    Returns:
      A scalar `Tensor` of type `string`. The serialized `tf.Summary` protocol
      buffer.
    """


def _strip_scope(name, scope, additional_scope):
  """Returns the name with scope stripped from it."""

  if additional_scope:
    name = name.replace("{}/".format(additional_scope), "")
  if not scope:
    scope = _DEFAULT_SCOPE
  name = name.replace("{}/".format(scope), "", 1)
  return name


class _ScopedSummary(Summary):
  """Records summaries in a given scope.

  Each scope gets assigned a different collection where summary ops gets added.

  This allows Tensorboard to display summaries with different scopes but the
  same name in the same charts.
  """

  def __init__(self, scope=None, skip_summary=False, namespace=None):
    """Initializes a `_ScopedSummary`.

    Args:
      scope: String scope name.
      skip_summary: Whether to record summary ops.
      namespace: Optional string namespace for the summary.

    Returns:
      A `_ScopedSummary` instance.
    """

    if tf_compat.tpu_function.get_tpu_context().number_of_shards:
      logging.log_first_n(
          logging.WARN,
          "Scoped summaries will be skipped since they do not support TPU", 1)
      skip_summary = True

    self._scope = scope
    self._namespace = namespace
    self._additional_scope = None
    self._skip_summary = skip_summary
    self._summary_ops = []
    self._actual_summary_scalar_fn = summary_lib.scalar
    self._actual_summary_image_fn = summary_lib.image
    self._actual_summary_histogram_fn = summary_lib.histogram
    self._actual_summary_audio_fn = summary_lib.audio

  @property
  def scope(self):
    """Returns scope string."""

    return self._scope

  @property
  def namespace(self):
    """Returns namespace string."""

    return self._namespace

  @contextlib.contextmanager
  def current_scope(self):
    """Registers the current context's scope to strip it from summary tags."""

    self._additional_scope = tf_compat.v1.get_default_graph().get_name_scope()
    yield
    self._additional_scope = None

  @contextlib.contextmanager
  def _strip_tag_scope(self):
    """Monkey patches `summary_op_util.summary_scope` to strip tag scopes."""

    original_summary_scope = summary_op_util.summary_scope

    @contextlib.contextmanager
    def strip_tag_scope_fn(name, family=None, default_name=None, values=None):
      tag, scope = (None, None)
      with original_summary_scope(name, family, default_name, values) as (t, s):
        tag = _strip_scope(t, self.scope, self._additional_scope)
        scope = s
      yield tag, scope

    summary_op_util.summary_scope = strip_tag_scope_fn
    yield
    summary_op_util.summary_scope = original_summary_scope

  def _prefix_scope(self, name):
    """Prefixes summary name with scope."""

    if self._scope:
      if name[0] == "/":
        name = name[1:]
      return "{scope}/{name}".format(scope=self._scope, name=name)
    return name

  def scalar(self, name, tensor, family=None):
    """See `Summary`."""

    if self._skip_summary:
      return tf.constant("")

    with self._strip_tag_scope():
      summary = self._actual_summary_scalar_fn(
          name=self._prefix_scope(name),
          tensor=tensor,
          family=family,
          collections=[])
    self._summary_ops.append(summary)
    return summary

  def image(self, name, tensor, max_outputs=3, family=None):
    """See `Summary`."""

    if self._skip_summary:
      return tf.constant("")

    with self._strip_tag_scope():
      summary = self._actual_summary_image_fn(
          name=self._prefix_scope(name),
          tensor=tensor,
          max_outputs=max_outputs,
          family=family,
          collections=[])
    self._summary_ops.append(summary)
    return summary

  def histogram(self, name, values, family=None):
    """See `Summary`."""

    if self._skip_summary:
      return tf.constant("")

    with self._strip_tag_scope():
      summary = self._actual_summary_histogram_fn(
          name=self._prefix_scope(name),
          values=values,
          family=family,
          collections=[])
    self._summary_ops.append(summary)
    return summary

  def audio(self, name, tensor, sample_rate, max_outputs=3, family=None):
    """See `Summary`."""

    if self._skip_summary:
      return tf.constant("")

    with self._strip_tag_scope():
      summary = self._actual_summary_audio_fn(
          name=self._prefix_scope(name),
          tensor=tensor,
          sample_rate=sample_rate,
          max_outputs=max_outputs,
          family=family,
          collections=[])
    self._summary_ops.append(summary)
    return summary

  def merge_all(self):
    """Returns the list of this graph's scoped summary ops.

    Note: this is an abuse of the tf.summary.merge_all API since it is expected
    to return a summary op with all summaries merged. However, ScopedSummary is
    only used in the internal implementation, so this should be OK.
    """

    current_graph = tf_compat.v1.get_default_graph()
    return [op for op in self._summary_ops if op.graph == current_graph]


# TODO: _ScopedSummary and _TPUScopedSummary share a lot of the same
# methods. Extract a base class for the two, or move shared methods into
# Summary.
class _TPUScopedSummary(Summary):
  """Records summaries in a given scope.

  Only for TPUEstimator.

  Each scope gets assigned a different collection where summary ops gets added.

  This allows Tensorboard to display summaries with different scopes but the
  same name in the same charts.
  """

  def __init__(self, logdir, namespace=None, scope=None, skip_summary=False):
    """Initializes a `_TPUScopedSummary`.

    Args:
      logdir: String directory path for logging summaries.
      namespace: String namespace to append to the logdir. Can be shared with
        other `_ScopedSummary` objects.
      scope: String scope name.
      skip_summary: Whether to record summary ops.

    Returns:
      A `_ScopedSummary` instance.
    """

    assert logdir

    if scope == _DEFAULT_SCOPE:
      raise ValueError("scope cannot be 'default'.")

    if namespace:
      logdir = os.path.join(logdir, namespace)
    if scope:
      logdir = os.path.join(logdir, scope)
    self._logdir = logdir
    self._namespace = namespace
    self._scope = scope
    self._additional_scope = None
    self._skip_summary = skip_summary
    self._actual_summary_scalar_fn = summary_v2_lib.scalar
    self._actual_summary_image_fn = summary_v2_lib.image
    self._actual_summary_histogram_fn = summary_v2_lib.histogram
    self._actual_summary_audio_fn = summary_v2_lib.audio
    self._summary_tuples = []

  @property
  def namespace(self):
    """Returns namespace string."""

    return self._namespace

  @property
  def scope(self):
    """Returns scope string."""

    return self._scope

  @property
  def logdir(self):
    """Returns the logdir."""

    return self._logdir

  @contextlib.contextmanager
  def current_scope(self):
    """Registers the current context's scope to strip it from summary tags."""

    self._additional_scope = tf_compat.v1.get_default_graph().get_name_scope()
    yield
    self._additional_scope = None

  @contextlib.contextmanager
  def _strip_tag_scope(self, additional_scope):
    """Monkey patches `summary_op_util.summary_scope` to strip tag scopes."""

    original_summary_scope = summary_op_util.summary_scope

    @contextlib.contextmanager
    def strip_tag_scope_fn(name, family=None, default_name=None, values=None):
      tag, scope = (None, None)
      with original_summary_scope(name, family, default_name, values) as (t, s):
        tag = _strip_scope(t, self.scope, additional_scope)
        scope = s
      yield tag, scope

    summary_op_util.summary_scope = strip_tag_scope_fn
    yield
    summary_op_util.summary_scope = original_summary_scope

  def _prefix_scope(self, name):
    scope = self._scope
    if not scope:
      scope = _DEFAULT_SCOPE
    if name[0] == "/":
      name = name[1:]
    return "{scope}/{name}".format(scope=scope, name=name)

  def _create_summary(self, summary_fn, name, tensor):
    """Creates a summary op.

    This will create a function that takes a `Tensor` and adds it to a list with
    its matching `tensor`.

    Args:
      summary_fn: A function that takes a name string and `Tensor` and returns a
        summary op.
      name: String name of the summary.
      tensor: `Tensor` to pass to the summary.
    """
    if self._skip_summary:
      return

    # additional_scope is set with the context from `current_scope`.
    # e.g. "foo/bar".
    additional_scope = self._additional_scope
    # name_scope is from whichever scope the summary actually gets called in.
    # e.g. "foo/bar/baz"
    name_scope = tf_compat.v1.get_default_graph().get_name_scope()
    # Reuse name_scope if it exists by appending "/" to it.
    name_scope = name_scope + "/" if name_scope else name_scope

    def _summary_fn(tensor, step):
      """Creates a summary with the given `Tensor`."""

      summary_name = self._prefix_scope(name)
      # Recover the current name scope when this fn is be called, because the
      # scope may be different when fns are called.
      # e.g. "foo/bar/baz/scalar" will become "baz/scalar" when
      # additional_scope is "foo/bar".
      # TODO: Figure out a cleaner way to handle this.
      assert not tf_compat.v1.get_default_graph().get_name_scope()
      with tf_compat.v1.name_scope(name_scope):
        with self._strip_tag_scope(additional_scope):
          # TODO: Do summaries need to be reduced before writing?
          # Presumably each tensor core creates its own summary so we may be
          # writing out num_tensor_cores copies of the same value.
          return summary_fn(summary_name, tensor, step)

    self._summary_tuples.append((_summary_fn, tensor))

  def scalar(self, name, tensor, family=None):

    def _summary_fn(name, tensor, step):
      return self._actual_summary_scalar_fn(
          name=name, tensor=tensor, family=family, step=step)

    self._create_summary(_summary_fn, name,
                         tf.reshape(tf.convert_to_tensor(value=tensor), [1]))

  def image(self, name, tensor, max_outputs=3, family=None):

    def _summary_fn(name, tensor, step):
      return self._actual_summary_image_fn(
          name=name,
          tensor=tensor,
          max_images=max_outputs,
          family=family,
          step=step)

    self._create_summary(_summary_fn, name, tf.cast(tensor, tf.float32))

  def histogram(self, name, values, family=None):

    def _summary_fn(name, tensor, step):
      return self._actual_summary_histogram_fn(
          name=name, tensor=tensor, family=family, step=step)

    self._create_summary(_summary_fn, name, tf.convert_to_tensor(value=values))

  def audio(self, name, tensor, sample_rate, max_outputs=3, family=None):

    def _summary_fn(name, tensor, step):
      return self._actual_summary_audio_fn(
          name=name,
          tensor=tensor,
          sample_rate=sample_rate,
          max_outputs=max_outputs,
          family=family,
          step=step)

    self._create_summary(_summary_fn, name, tf.cast(tensor, tf.float32))

  def summary_tuples(self):
    """Returns an iterable of functions that convert a Tensor to a summary.

    Used for TPU host calls.

    Returns:
      Iterable of functions that take a single `Tensor` argument.
    """
    return tuple(self._summary_tuples)

  def clear_summary_tuples(self):
    """Clears the list of current summary tuples."""

    self._summary_tuples = []


class _SummaryWrapper(object):
  """Wraps an `adanet.Summary` to provide summary-like APIs."""

  def __init__(self, summary):
    self._summary = summary

  def scalar(self, name, tensor, collections=None, family=None):
    """See `tf.summary.scalar`."""

    if collections is not None:
      logging.warning(
          "The `collections` argument will be "
          "ignored for scalar summary: %s, %s", name, tensor)
    return self._summary.scalar(name=name, tensor=tensor, family=family)

  def image(self, name, tensor, max_outputs=3, collections=None, family=None):
    """See `tf.summary.image`."""

    if collections is not None:
      logging.warning(
          "The `collections` argument will be "
          "ignored for image summary: %s, %s", name, tensor)
    return self._summary.image(
        name=name, tensor=tensor, max_outputs=max_outputs, family=family)

  def histogram(self, name, values, collections=None, family=None):
    """See `tf.summary.histogram`."""

    if collections is not None:
      logging.warning(
          "The `collections` argument will be "
          "ignored for histogram summary: %s, %s", name, values)
    return self._summary.histogram(name=name, values=values, family=family)

  def audio(self,
            name,
            tensor,
            sample_rate,
            max_outputs=3,
            collections=None,
            family=None):
    """See `tf.summary.audio`."""

    if collections is not None:
      logging.warning(
          "The `collections` argument will be "
          "ignored for audio summary: %s, %s", name, tensor)
    return self._summary.audio(
        name=name,
        tensor=tensor,
        sample_rate=sample_rate,
        max_outputs=max_outputs,
        family=family)

  def scalar_v2(self, name, tensor, family=None, step=None):
    """See `tf.contrib.summary.scalar`."""

    if step is not None:
      logging.warning(
          "The `step` argument will be ignored to use the global step for "
          "scalar summary: %s, %s", name, tensor)
    return self._summary.scalar(name=name, tensor=tensor, family=family)

  def image_v2(self,
               name,
               tensor,
               bad_color=None,
               max_images=3,
               family=None,
               step=None):
    """See `tf.contrib.summary.image`."""

    if step is not None:
      logging.warning(
          "The `step` argument will be ignored to use the global step for "
          "image summary: %s, %s", name, tensor)
    # TODO: Add support for `bad_color` arg.
    if bad_color is not None:
      logging.warning(
          "The `bad_color` arg is not supported for image summary: %s, %s",
          name, tensor)
    return self._summary.image(
        name=name, tensor=tensor, max_outputs=max_images, family=family)

  def histogram_v2(self, name, tensor, family=None, step=None):
    """See `tf.contrib.summary.histogram`."""

    if step is not None:
      logging.warning(
          "The `step` argument will be ignored to use the global step for "
          "histogram summary: %s, %s", name, tensor)
    return self._summary.histogram(name=name, values=tensor, family=family)

  def audio_v2(self,
               name,
               tensor,
               sample_rate,
               max_outputs,
               family=None,
               step=None):
    """See `tf.contrib.summary.audio`."""

    if step is not None:
      logging.warning(
          "The `step` argument will be ignored to use the global step for "
          "audio summary: %s, %s", name, tensor)
    return self._summary.audio(
        name=name,
        tensor=tensor,
        sample_rate=sample_rate,
        max_outputs=max_outputs,
        family=family)


@contextlib.contextmanager
def monkey_patched_summaries(summary):
  """A context where global summary functions point to the given summary.

  Restores original summary functions upon exit.

  NOTE: This function is not thread-safe.

  Args:
    summary: An `adanet.Summary` instance.

  Yields:
    A context where summary functions are routed to the given `adanet.Summary`.
  """

  old_summary_scalar = summary_lib.scalar
  old_summary_image = summary_lib.image
  old_summary_histogram = summary_lib.histogram
  old_summary_audio = summary_lib.audio
  old_summary_v2_scalar = summary_v2_lib.scalar
  old_summary_v2_image = summary_v2_lib.image
  old_summary_v2_histogram = summary_v2_lib.histogram
  old_summary_v2_audio = summary_v2_lib.audio
  old_summary_compat_v2_scalar = tf_compat.v2.summary.scalar
  old_summary_compat_v2_image = tf_compat.v2.summary.image
  old_summary_compat_v2_histogram = tf_compat.v2.summary.histogram
  old_summary_compat_v2_audio = tf_compat.v2.summary.audio

  # Monkey-patch global attributes.
  wrapped_summary = _SummaryWrapper(summary)
  setattr(tf.summary, "scalar", wrapped_summary.scalar)
  setattr(tf.summary, "image", wrapped_summary.image)
  setattr(tf.summary, "histogram", wrapped_summary.histogram)
  setattr(tf.summary, "audio", wrapped_summary.audio)
  setattr(tf_compat.v1.summary, "scalar", wrapped_summary.scalar)
  setattr(tf_compat.v1.summary, "image", wrapped_summary.image)
  setattr(tf_compat.v1.summary, "histogram", wrapped_summary.histogram)
  setattr(tf_compat.v1.summary, "audio", wrapped_summary.audio)
  setattr(summary_lib, "scalar", wrapped_summary.scalar)
  setattr(summary_lib, "image", wrapped_summary.image)
  setattr(summary_lib, "histogram", wrapped_summary.histogram)
  setattr(summary_lib, "audio", wrapped_summary.audio)
  setattr(tf_compat.v2.summary, "scalar", wrapped_summary.scalar_v2)
  setattr(tf_compat.v2.summary, "image", wrapped_summary.image_v2)
  setattr(tf_compat.v2.summary, "histogram", wrapped_summary.histogram_v2)
  setattr(tf_compat.v2.summary, "audio", wrapped_summary.audio_v2)
  setattr(summary_v2_lib, "scalar", wrapped_summary.scalar_v2)
  setattr(summary_v2_lib, "image", wrapped_summary.image_v2)
  setattr(summary_v2_lib, "histogram", wrapped_summary.histogram_v2)
  setattr(summary_v2_lib, "audio", wrapped_summary.audio_v2)
  try:
    # TF 2.0 eliminates tf.contrib.
    setattr(tf.contrib.summary, "scalar", wrapped_summary.scalar_v2)
    setattr(tf.contrib.summary, "image", wrapped_summary.image_v2)
    setattr(tf.contrib.summary, "histogram", wrapped_summary.histogram_v2)
    setattr(tf.contrib.summary, "audio", wrapped_summary.audio_v2)
  except AttributeError:
    # TF 2.0 eliminates tf.contrib.
    pass

  try:
    yield
  finally:
    # Revert monkey-patches.
    try:
      setattr(tf.contrib.summary, "audio", old_summary_v2_audio)
      setattr(tf.contrib.summary, "histogram", old_summary_v2_histogram)
      setattr(tf.contrib.summary, "image", old_summary_v2_image)
      setattr(tf.contrib.summary, "scalar", old_summary_v2_scalar)
    except AttributeError:
      # TF 2.0 eliminates tf.contrib.
      pass
    setattr(summary_v2_lib, "audio", old_summary_v2_audio)
    setattr(summary_v2_lib, "histogram", old_summary_v2_histogram)
    setattr(summary_v2_lib, "image", old_summary_v2_image)
    setattr(summary_v2_lib, "scalar", old_summary_v2_scalar)
    setattr(tf_compat.v2.summary, "audio", old_summary_compat_v2_audio)
    setattr(tf_compat.v2.summary, "histogram", old_summary_compat_v2_histogram)
    setattr(tf_compat.v2.summary, "image", old_summary_compat_v2_image)
    setattr(tf_compat.v2.summary, "scalar", old_summary_compat_v2_scalar)
    setattr(summary_lib, "audio", old_summary_audio)
    setattr(summary_lib, "histogram", old_summary_histogram)
    setattr(summary_lib, "image", old_summary_image)
    setattr(summary_lib, "scalar", old_summary_scalar)
    setattr(tf_compat.v1.summary, "audio", old_summary_audio)
    setattr(tf_compat.v1.summary, "histogram", old_summary_histogram)
    setattr(tf_compat.v1.summary, "image", old_summary_image)
    setattr(tf_compat.v1.summary, "scalar", old_summary_scalar)
    setattr(tf.summary, "audio", old_summary_audio)
    setattr(tf.summary, "histogram", old_summary_histogram)
    setattr(tf.summary, "image", old_summary_image)
    setattr(tf.summary, "scalar", old_summary_scalar)
