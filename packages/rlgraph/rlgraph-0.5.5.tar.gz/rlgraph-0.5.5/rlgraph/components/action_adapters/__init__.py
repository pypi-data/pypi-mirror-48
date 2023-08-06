# Copyright 2018/2019 The RLgraph authors, All Rights Reserved.
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

from rlgraph.components.action_adapters.action_adapter import ActionAdapter
from rlgraph.components.action_adapters.action_adapter_utils import get_action_adapter_type_from_distribution_type, \
    get_distribution_spec_from_action_adapter
from rlgraph.components.action_adapters.bernoulli_distribution_adapter import BernoulliDistributionAdapter
from rlgraph.components.action_adapters.beta_distribution_adapter import BetaDistributionAdapter
from rlgraph.components.action_adapters.categorical_distribution_adapter import CategoricalDistributionAdapter
from rlgraph.components.action_adapters.gumbel_softmax_distribution_adapter import GumbelSoftmaxDistributionAdapter
from rlgraph.components.action_adapters.normal_distribution_adapter import NormalDistributionAdapter
from rlgraph.components.action_adapters.squashed_normal_distribution_adapter import SquashedNormalDistributionAdapter

ActionAdapter.__lookup_classes__ = dict(
    actionadapter=ActionAdapter,
    bernoullidistributionadapter=BernoulliDistributionAdapter,
    categoricaldistributionadapter=CategoricalDistributionAdapter,
    betadistributionadapter=BetaDistributionAdapter,
    gumbelsoftmaxdistributionadapter=GumbelSoftmaxDistributionAdapter,
    gumbelsoftmaxadapter=GumbelSoftmaxDistributionAdapter,
    normaldistributionadapter=NormalDistributionAdapter,
    squashednormaladapter=SquashedNormalDistributionAdapter,
    squashednormaldistributionadapter=SquashedNormalDistributionAdapter,
)

__all__ = ["ActionAdapter", "get_action_adapter_type_from_distribution_type",
           "get_distribution_spec_from_action_adapter"] + \
          list(set(map(lambda x: x.__name__, ActionAdapter.__lookup_classes__.values())))
