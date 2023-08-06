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

from rlgraph.utils.define_by_run_ops import print_call_chain
from rlgraph.utils.initializer import Initializer
from rlgraph.utils.numpy import sigmoid, softmax, relu, one_hot
from rlgraph.utils.ops import DataOp, SingleDataOp, DataOpDict, DataOpTuple, ContainerDataOp, FlattenedDataOp
from rlgraph.utils.pytorch_util import pytorch_one_hot, PyTorchVariable
from rlgraph.utils.rlgraph_errors import RLGraphError, RLGraphAPICallParamError, RLGraphBuildError, \
    RLGraphInputIncompleteError, RLGraphVariableIncompleteError, RLGraphObsoletedError, RLGraphSpaceError
from rlgraph.utils.specifiable import Specifiable
from rlgraph.utils.util import convert_dtype, get_shape, get_rank, force_tuple, force_list, \
    LARGE_INTEGER, SMALL_NUMBER, MIN_LOG_STDDEV, MAX_LOG_STDDEV, \
    tf_logger, print_logging_handler, root_logger, logging_formatter, default_dict

# from rlgraph.utils.specifiable_server import SpecifiableServer, SpecifiableServerHook
#from rlgraph.utils.decorators import api


__all__ = [
    "RLGraphError", "RLGraphAPICallParamError", "RLGraphBuildError",
    "RLGraphInputIncompleteError", "RLGraphVariableIncompleteError", "RLGraphObsoletedError", "RLGraphSpaceError",
    "Initializer", "Specifiable", "convert_dtype", "get_shape", "get_rank", "force_tuple", "force_list",
    "logging_formatter", "root_logger", "tf_logger", "print_logging_handler", "sigmoid", "softmax", "relu", "one_hot",
    "DataOp", "SingleDataOp", "DataOpDict", "DataOpTuple", "ContainerDataOp", "FlattenedDataOp",
    "pytorch_one_hot", "PyTorchVariable", "LARGE_INTEGER", "SMALL_NUMBER", "MIN_LOG_STDDEV", "MAX_LOG_STDDEV"
]
