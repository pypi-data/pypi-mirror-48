# Copyright 2018/2019 The RLgraph authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import, division, print_function

from rlgraph.components.neural_networks.stack import Stack
from rlgraph.components.neural_networks.dict_preprocessor_stack import DictPreprocessorStack
from rlgraph.components.neural_networks.preprocessor_stack import PreprocessorStack
from rlgraph.components.neural_networks.neural_network import NeuralNetwork
from rlgraph.components.neural_networks.multi_input_stream_neural_network import MultiInputStreamNeuralNetwork
from rlgraph.components.neural_networks.variational_auto_encoder import VariationalAutoEncoder
from rlgraph.components.neural_networks.value_function import ValueFunction
from rlgraph.components.neural_networks.sac.sac_networks import SACValueNetwork

# NeuralNetworks
NeuralNetwork.__lookup_classes__ = dict(
    neuralnetwork=NeuralNetwork,
    multiinputstreamneuralnetwork=MultiInputStreamNeuralNetwork,
    multiinputstreamnn=MultiInputStreamNeuralNetwork,
    variationalautoencoder=VariationalAutoEncoder
)

# The Stacks.
Stack.__lookup_classes__ = dict(
    dictpreprocessorstack=DictPreprocessorStack,
    preprocessorstack=PreprocessorStack
)

ValueFunction.__lookup_classes__ = dict(
    sacvaluefunction=SACValueNetwork,
    valuefunction=ValueFunction,
)
ValueFunction.__default_constructor__ = ValueFunction


__all__ = ["NeuralNetwork", "ValueFunction"] + \
          ["Stack"] + \
          list(set(map(lambda x: x.__name__, NeuralNetwork.__lookup_classes__.values()))) + \
          list(set(map(lambda x: x.__name__, Stack.__lookup_classes__.values()))) + \
          list(set(map(lambda x: x.__name__, ValueFunction.__lookup_classes__.values())))


