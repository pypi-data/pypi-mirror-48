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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from rlgraph import get_backend
from rlgraph.components.distributions.distribution import Distribution
from rlgraph.utils import util
from rlgraph.utils.decorators import rlgraph_api, graph_fn

if get_backend() == "tf":
    import tensorflow as tf
    import tensorflow_probability as tfp
elif get_backend() == "pytorch":
    import torch


class Categorical(Distribution):
    """
    A categorical distribution object defined by a n values {p0, p1, ...} that add up to 1, the probabilities
    for picking one of the n categories.
    """
    def __init__(self, scope="categorical", **kwargs):
        super(Categorical, self).__init__(scope=scope, **kwargs)

    @rlgraph_api
    def _graph_fn_get_distribution(self, parameters):
        if get_backend() == "tf":
            return tfp.distributions.Categorical(logits=parameters, dtype=util.convert_dtype("int"))
        elif get_backend() == "pytorch":
            return torch.distributions.Categorical(logits=parameters)

    @graph_fn
    def _graph_fn_sample_deterministic(self, distribution):
        if get_backend() == "tf":
            return tf.argmax(input=distribution.probs, axis=-1, output_type=util.convert_dtype("int"))
        elif get_backend() == "pytorch":
            return torch.argmax(distribution.probs, dim=-1).int()
