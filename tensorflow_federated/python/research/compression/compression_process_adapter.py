# Copyright 2020, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Adapter to map between TFF compression processes and python containers."""

import collections

import tensorflow_federated as tff

from tensorflow_federated.python.research.utils import adapters

ModelWeights = collections.namedtuple('ModelWeights', 'trainable non_trainable')


class CompressionServerState(tff.learning.framework.ServerState):
  """Represents the state of the server carried between rounds."""

  @classmethod
  def assign_weights_to_keras_model(cls, reference_model, keras_model):
    """Assign the model weights to the weights of a `tf.keras.Model`.

    Args:
      reference_model: the `ModelWeights` object to assign weights from.
      keras_model: the `tf.keras.Model` object to assign weights to.
    """
    if not isinstance(reference_model, ModelWeights):
      raise TypeError('Reference model must be an instance of '
                      'compression_process_adapter.ModelWeights.')

    def assign_weights(keras_weights, tff_weights):
      for k, w in zip(keras_weights, tff_weights):
        k.assign(w)

    assign_weights(keras_model.trainable_weights, reference_model.trainable)
    assign_weights(keras_model.non_trainable_weights,
                   reference_model.non_trainable)


class CompressionProcessAdapter(adapters.IterativeProcessPythonAdapter):
  """Converts iterative process results from anonymous tuples.

  Intended to be used for iterative processes returned by
  `tff.learning.framework.build_model_delta_optimizer_process`. Note
  that this is also called by `tff.learning.build_federated_averaging_process`.
  """

  def __init__(self, iterative_process):
    self._iterative_process = iterative_process

  def initialize(self):
    return self._iterative_process.initialize()

  def next(self, state, data):
    state, metrics = self._iterative_process.next(state, data)
    outputs = None
    return adapters.IterationResult(state, metrics, outputs)
