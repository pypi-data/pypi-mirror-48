"""An estimator that learns to ensemble.

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

import collections

from adanet import tf_compat
from adanet.core import Estimator
from adanet.subnetwork import Builder
from adanet.subnetwork import Generator
from adanet.subnetwork import Subnetwork
from adanet.subnetwork import TrainOpSpec
import tensorflow as tf

from tensorflow.python.estimator.canned import prediction_keys


def _default_logits(estimator_spec):
  if isinstance(estimator_spec.predictions, dict):
    pred_keys = prediction_keys.PredictionKeys
    if pred_keys.LOGITS in estimator_spec.predictions:
      return estimator_spec.predictions[pred_keys.LOGITS]
    if pred_keys.PREDICTIONS in estimator_spec.predictions:
      return estimator_spec.predictions[pred_keys.PREDICTIONS]
  return estimator_spec.predictions


class AutoEnsembleSubestimator(
    collections.namedtuple("AutoEnsembleSubestimator",
                           ["estimator", "train_input_fn"])):
  """A subestimator to train and consider for ensembling.

  Args:
    estimator: A `tf.estimator.Estimator` instance to consider for ensembling.
    train_input_fn: A function that provides input data for training as
      minibatches. It can be used to implement ensemble methods like bootstrap
      aggregating (a.k.a bagging) where each subnetwork trains on different
      slices of the training data. The function should construct and return one
      of the following:
       * A `tf.data.Dataset` object: Outputs of `Dataset` object must be a tuple
         `(features, labels)` with same constraints as below.
       * A tuple `(features, labels)`: Where `features` is a `tf.Tensor` or a
         dictionary of string feature name to `Tensor` and `labels` is a
         `Tensor` or a dictionary of string label name to `Tensor`. Both
         `features` and `labels` are consumed by `estimator#model_fn`. They
         should satisfy the expectation of `estimator#model_fn` from inputs.

  Returns:
    An `AutoEnsembleSubestimator` instance to be auto-ensembled.
  """

  def __new__(cls, estimator, train_input_fn=None):
    return super(AutoEnsembleSubestimator, cls).__new__(cls, estimator,
                                                        train_input_fn)


class _BuilderFromSubestimator(Builder):
  """An `adanet.Builder` from a :class:`tf.estimator.Estimator`."""

  def __init__(self, name, subestimator, logits_fn, config):
    self._name = name
    self._subestimator = subestimator
    self._logits_fn = logits_fn
    self._config = config

  @property
  def name(self):
    return self._name

  def _call_model_fn(self, features, labels, mode):
    model_fn = self._subestimator.estimator.model_fn
    estimator_spec = model_fn(
        features=features, labels=labels, mode=mode, config=self._config)
    logits = self._logits_fn(estimator_spec=estimator_spec)
    train_op = TrainOpSpec(
        estimator_spec.train_op,
        chief_hooks=estimator_spec.training_chief_hooks,
        hooks=estimator_spec.training_hooks)
    return logits, train_op

  def build_subnetwork(self, features, labels, logits_dimension, training,
                       iteration_step, summary, previous_ensemble):
    # We don't need an EVAL mode since AdaNet takes care of evaluation for us.
    mode = tf.estimator.ModeKeys.PREDICT
    if training:
      mode = tf.estimator.ModeKeys.TRAIN

    # Call in template to ensure that variables are created once and reused.
    call_model_fn_template = tf.make_template("model_fn", self._call_model_fn)
    subestimator_features, subestimator_labels = features, labels
    if training and self._subestimator.train_input_fn:
      # TODO: Consider tensorflow_estimator/python/estimator/util.py.
      inputs = self._subestimator.train_input_fn()
      if isinstance(inputs, (tf_compat.DatasetV1, tf_compat.DatasetV2)):
        subestimator_features, subestimator_labels = tf_compat.make_one_shot_iterator(
            inputs).get_next()
      else:
        subestimator_features, subestimator_labels = inputs

      # Construct subnetwork graph first because of dependencies on scope.
      _, train_op = call_model_fn_template(subestimator_features,
                                           subestimator_labels, mode)
      # Graph for ensemble learning gets model_fn_1 for scope.
      logits, _ = call_model_fn_template(features, labels, mode)
    else:
      logits, train_op = call_model_fn_template(features, labels, mode)

    # TODO: Replace with variance complexity measure.
    complexity = tf.constant(0.)
    return Subnetwork(
        logits=logits,
        last_layer=logits,
        shared={"train_op": train_op},
        complexity=complexity)

  def build_subnetwork_train_op(self, subnetwork, loss, var_list, labels,
                                iteration_step, summary, previous_ensemble):
    return subnetwork.shared["train_op"]


def _convert_to_subestimator(candidate):
  if isinstance(candidate, AutoEnsembleSubestimator):
    return candidate
  if isinstance(candidate, tf.estimator.Estimator):
    return AutoEnsembleSubestimator(candidate)
  raise ValueError(
      "subestimator in candidate_pool must have type tf.estimator.Estimator or "
      "adanet.AutoEnsembleSubestimator but got {}".format(candidate.__class__))


class _GeneratorFromCandidatePool(Generator):
  """An `adanet.Generator` from a pool of `Estimator` and `Model` instances."""

  def __init__(self, candidate_pool, logits_fn):
    self._candidate_pool = candidate_pool
    if logits_fn is None:
      logits_fn = _default_logits
    self._logits_fn = logits_fn

  def generate_candidates(self, previous_ensemble, iteration_number,
                          previous_ensemble_reports, all_reports, config):
    assert config
    builders = []
    candidate_pool = self._candidate_pool
    if callable(candidate_pool):
      # candidate_pool can be a function.
      candidate_pool = candidate_pool(config=config)
    if isinstance(candidate_pool, dict):
      for name in sorted(candidate_pool):
        builders.append(
            _BuilderFromSubestimator(
                name,
                _convert_to_subestimator(candidate_pool[name]),
                logits_fn=self._logits_fn,
                config=config))
      return builders

    for i, estimator in enumerate(candidate_pool):
      name = "{class_name}{index}".format(
          class_name=estimator.__class__.__name__, index=i)
      builders.append(
          _BuilderFromSubestimator(
              name,
              _convert_to_subestimator(estimator),
              logits_fn=self._logits_fn,
              config=config))
    return builders


class AutoEnsembleEstimator(Estimator):
  # pyformat: disable
  """A :class:`tf.estimator.Estimator` that learns to ensemble models.

  Specifically, it learns to ensemble models from a candidate pool using the
  Adanet algorithm.

  .. code-block:: python

      # A simple example of learning to ensemble linear and neural network
      # models.

      import adanet
      import tensorflow as tf

      feature_columns = ...

      head = MultiClassHead(n_classes=10)

      # Learn to ensemble linear and DNN models.
      estimator = adanet.AutoEnsembleEstimator(
          head=head,
          candidate_pool=lambda config: {
              "linear":
                  tf.estimator.LinearEstimator(
                      head=head,
                      feature_columns=feature_columns,
                      config=config,
                      optimizer=...),
              "dnn":
                  tf.estimator.DNNEstimator(
                      head=head,
                      feature_columns=feature_columns,
                      config=config,
                      optimizer=...,
                      hidden_units=[1000, 500, 100])},
          max_iteration_steps=50)

      # Input builders
      def input_fn_train:
        # Returns tf.data.Dataset of (x, y) tuple where y represents label's
        # class index.
        pass
      def input_fn_eval:
        # Returns tf.data.Dataset of (x, y) tuple where y represents label's
        # class index.
        pass
      def input_fn_predict:
        # Returns tf.data.Dataset of (x, None) tuple.
        pass
      estimator.train(input_fn=input_fn_train, steps=100)
      metrics = estimator.evaluate(input_fn=input_fn_eval, steps=10)
      predictions = estimator.predict(input_fn=input_fn_predict)

  Or to train candidate subestimators on different training data subsets:

  .. code-block:: python

      train_data_files = [...]

      # Learn to ensemble linear and DNN models.
      estimator = adanet.AutoEnsembleEstimator(
          head=head,
          candidate_pool=lambda config: {
              "linear":
                  adanet.AutoEnsembleSubestimator(
                      tf.estimator.LinearEstimator(
                          head=head,
                          feature_columns=feature_columns,
                          config=config,
                          optimizer=...),
                      make_train_input_fn(train_data_files[:-1])),
              "dnn":
                  adanet.AutoEnsembleSubestimator(
                      tf.estimator.DNNEstimator(
                          head=head,
                          feature_columns=feature_columns,
                          config=config,
                          optimizer=...,
                          hidden_units=[1000, 500, 100]),
                      make_train_input_fn(train_data_files[0:]))},
          max_iteration_steps=50)

      estimator.train(input_fn=make_train_input_fn(train_data_files), steps=100)


  Args:
    head: A :class:`tf.contrib.estimator.Head` instance for computing loss and
      evaluation metrics for every candidate.
    candidate_pool: List of :class:`tf.estimator.Estimator` and
      :class:`AutoEnsembleSubestimator` objects, or dict of string name to
      :class:`tf.estimator.Estimator` and :class:`AutoEnsembleSubestimator`
      objects that are candidate subestimators to ensemble at each iteration.
      The order does not directly affect which candidates will be included in
      the final ensemble, but will affect the name of the candidate. When using
      a dict, the string key becomes the candidate subestimator's name.
      Alternatively, this argument can be a function that takes a `config`
      argument and returns the aforementioned values in case the
      objects need to be re-instantiated at each adanet iteration.
    max_iteration_steps: Total number of steps for which to train candidates per
      iteration. If `OutOfRange` or `StopIteration` occurs in the middle,
      training stops before `max_iteration_steps` steps.
    logits_fn: A function for fetching the subnetwork logits from a
      :class:`tf.estimator.EstimatorSpec`, which should obey the following
      signature:
        - `Args`: Can only have following argument:
          - estimator_spec: The candidate's :class:`tf.estimator.EstimatorSpec`.
        - `Returns`: Logits :class:`tf.Tensor` or dict of string to logits
          :class:`tf.Tensor` (for multi-head) for the candidate subnetwork
          extracted from the given `estimator_spec`. When `None`, it will
          default to returning `estimator_spec.predictions` when they are a
          :class:`tf.Tensor` or the :class:`tf.Tensor` for the key 'logits' when
          they are a dict of string to :class:`tf.Tensor`.
    ensemblers: See :class:`adanet.Estimator`.
    ensemble_strategies: See :class:`adanet.Estimator`.
    evaluator:  See :class:`adanet.Estimator`.
    metric_fn:  See :class:`adanet.Estimator`.
    force_grow:  See :class:`adanet.Estimator`.
    adanet_loss_decay: See :class:`adanet.Estimator`.
    worker_wait_timeout_secs: See :class:`adanet.Estimator`.
    model_dir: See :class:`adanet.Estimator`.
    config: See :class:`adanet.Estimator`.
    debug: See :class:`adanet.Estimator`.

  Returns:
    An :class:`adanet.AutoEnsembleEstimator` instance.

  Raises:
    ValueError: If any of the candidates in `candidate_pool` are not
      :class:`tf.estimator.Estimator` instances.
  """
  # pyformat: enable

  def __init__(self,
               head,
               candidate_pool,
               max_iteration_steps,
               ensemblers=None,
               ensemble_strategies=None,
               logits_fn=None,
               evaluator=None,
               metric_fn=None,
               force_grow=False,
               adanet_loss_decay=.9,
               worker_wait_timeout_secs=7200,
               model_dir=None,
               config=None,
               **kwargs):
    subnetwork_generator = _GeneratorFromCandidatePool(candidate_pool,
                                                       logits_fn)
    super(AutoEnsembleEstimator, self).__init__(
        head=head,
        subnetwork_generator=subnetwork_generator,
        max_iteration_steps=max_iteration_steps,
        ensemblers=ensemblers,
        ensemble_strategies=ensemble_strategies,
        evaluator=evaluator,
        metric_fn=metric_fn,
        force_grow=force_grow,
        adanet_loss_decay=adanet_loss_decay,
        worker_wait_timeout_secs=worker_wait_timeout_secs,
        model_dir=model_dir,
        config=config,
        **kwargs)
