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

import os.path

from rlgraph import get_backend
from rlgraph.components.common.synchronizable import Synchronizable
from rlgraph.components.neural_networks.value_function import ValueFunction
from rlgraph.utils.rlgraph_errors import RLGraphError
from rlgraph.utils.util import default_dict


def parse_saver_spec(saver_spec):
    """
    Parses the saver spec. Returns None if input None, otherwise
    provides default parameters.

    Args:
        saver_spec (Union[None, dict]): Saver parameters.

    Returns:
        Union(dict, None): Saver spec or None.
    """

    if saver_spec is None:
        return None
    default_spec = dict(
        # The directory in which to store model checkpoint files.
        directory=os.path.expanduser("~/rlgraph_checkpoints/"),  # default=home dir
        # The base file name for a saved checkpoint.
        checkpoint_basename="model.ckpt",
        # How many files to maximally store for one graph.
        max_checkpoints=5,
        # Every how many seconds do we save? None if saving frequency should be step based.
        save_secs=600,
        # Every how many steps do we save? None if saving frequency should be time (seconds) based.
        save_steps=None
    )
    return default_dict(saver_spec, default_spec)


def parse_value_function_spec(value_function_spec):
    """
    Creates value function from spec if needed.

    Args:
        value_function_spec (list, dict, ValueFunction): Neural network specification for baseline or instance
            of ValueFunction.
    Returns:
        Optional(ValueFunction): None if Spec is None or instance of ValueFunction.
    """
    if value_function_spec is None:
        return None
    else:
        vf_sync = Synchronizable()
        # VF is already instantiated.
        if isinstance(value_function_spec, ValueFunction):
            value_function = value_function_spec
            if vf_sync.name not in value_function.sub_components:
                value_function.add_components(vf_sync, expose_apis="sync")
        else:
            if isinstance(value_function_spec, list):
                # Use default type if given is layer-list.
                value_function_spec = dict(type="value_function", network_spec=value_function_spec)
            value_function = ValueFunction.from_spec(value_function_spec)
            value_function.add_components(vf_sync, expose_apis="sync")
        return value_function


def parse_summary_spec(summary_spec):
    """
    Expands summary spec with default values where necessary.

    Args:
        summary_spec (dict): Summary options.

    Returns:
        dict: Summary spec updated with default values.
    """
    default_spec = dict(
        # The directory in which to store the summary files.
        directory=os.path.expanduser("~/rlgraph_summaries/"),  # default=home dir
        # A regexp pattern that a summary op (including its global scope) has to match in order for it to
        # be included in the graph's summaries.
        summary_regexp=None,
        # Every how many seconds do we save a summary? None if saving frequency should be step based.
        save_secs=120,
        # Every how many steps do we save a summary? None if saving frequency should be time (seconds) based.
        save_steps=None
    )
    return default_dict(summary_spec, default_spec)


def parse_execution_spec(execution_spec):
    """
    Parses execution parameters and inserts default values where necessary.

    Args:
        execution_spec (Optional[dict]): Execution spec dict. Must specify an execution mode
            "single" or "distributed". If mode "distributed", must specify a "distributed_spec"
            containing:
             - a key cluster_spec mapping to a ClusterSpec object,
             - a "job" for the job name,
             - an integer "task_index"

    Returns:
        dict: The sanitized execution_spec dict.
    """
    # TODO these are tensorflow specific
    # If no spec given.
    if get_backend() == "tf":
        default_spec = dict(
            mode="single",
            distributed_spec=None,
            # Using a monitored session enabling summaries and hooks per default.
            disable_monitoring=False,
            # Gpu settings.
            gpu_spec=dict(
                # Are GPUs allowed to be used if they are detected?
                gpus_enabled=False,
                # If yes, how many GPUs are to be used?
                max_usable_gpus=0,
                # If True, use `max_usable_gpus` fake-GPUs (CPU) iff no GPUs are available.
                fake_gpus_if_necessary=False,
                # Specify specific CUDA devices to be used, e.g. gpu 0 and 2 = [0, 2].
                # If None, we use CUDA devices [0, max_usable_gpus - 1]
                cuda_devices=None,
                # Fraction of the overall amount of memory that each visible GPU should be allocated.
                per_process_gpu_memory_fraction=None,
                # If True, not all memory will be allocated which is relevant on shared resources.
                allow_memory_growth=False
            ),
            # Device placement settings.
            device_strategy="default",
            default_device=None,
            device_map={},

            session_config=None,
            # Random seed for the tf graph.
            seed=None,
            # Enabling the tf profiler?
            enable_profiler=False,
            # With which frequency do we print out profiler information?
            profiler_frequency=1000,
            # Enabling a timeline write?
            enable_timeline=False,
            # With which frequency do we write out a timeline file?
            timeline_frequency=1,
        )
        execution_spec = default_dict(execution_spec, default_spec)

        # Sub specifications:

        # Distributed specifications.
        if execution_spec.get("mode") == "distributed":
            default_distributed = dict(
                job="ps",
                task_index=0,
                cluster_spec=dict(
                    ps=["localhost:22222"],
                    worker=["localhost:22223"]
                ),
                protocol=None
            )
            execution_spec["distributed_spec"] = default_dict(execution_spec.get("distributed_spec"), default_distributed)

        # Session config.
        default_session_config = dict(
            type="monitored-training-session",
            allow_soft_placement=True,
            log_device_placement=False
        )
        execution_spec["session_config"] = default_dict(execution_spec.get("session_config"), default_session_config)
    elif get_backend() == "pytorch":
        # No session configs, different GPU options.
        default_spec = dict(
            mode="single",
            distributed_spec=None,
            # Using a monitored session enabling summaries and hooks per default.
            disable_monitoring=False,
            # Gpu settings.
            gpu_spec=dict(
                # Are GPUs allowed to be used if they are detected?
                gpus_enabled=False,
                # If yes, how many GPUs are to be used?
                max_usable_gpus=0,
                # Specify specific CUDA devices to be used, e.g. gpu 0 and 2 = [0, 2].
                # If None, we use CUDA devices [0, max_usable_gpus - 1]
                cuda_devices=None
            ),
            # Device placement settings.
            device_strategy="default",
            default_device=None,
            device_map={},
            # TODO potentially set to nproc?
            torch_num_threads=1,
            OMP_NUM_THREADS=1
        )
        execution_spec = default_dict(execution_spec, default_spec)

    return execution_spec


def parse_observe_spec(observe_spec):
    """
    Parses parameters for `Agent.observe()` calls and inserts default values where necessary.

    Args:
        observe_spec (Optional[dict]): Observe spec dict.

    Returns:
        dict: The sanitized observe_spec dict.
    """
    if observe_spec and "buffer_enabled" not in observe_spec:
        # Set to true if a buffer size is given and > 0, but flag is not given.
        if "buffer_size" in observe_spec and observe_spec["buffer_size"] > 0:
            observe_spec["buffer_enabled"] = True

    # If no spec given.
    default_spec = dict(
        # Do we buffer observations in python before sending them through the graph?
        buffer_enabled=False,
        # Fill buffer with n records before sending them through the graph.
        buffer_size=100,  # only if buffer_enabled=True
        # Set to > 1 if we want to post-process buffered values for n-step learning.
        n_step=1,  # values > 1 are only allowed if buffer_enabled is True and buffer_size >> n.
    )
    observe_spec = default_dict(observe_spec, default_spec)

    if observe_spec["n_step"] > 1:
        if observe_spec["buffer_enabled"] is False:
            raise RLGraphError(
                "Cannot setup observations with n-step (n={}), while buffering is switched "
                "off".format(observe_spec["n_step"])
            )
        elif observe_spec["buffer_size"] < 3 * observe_spec["n_step"]:
            raise RLGraphError(
                "Buffer must be at least 3x as large as n-step (n={}, min-buffer={})!".format(
                    observe_spec["n_step"], 3 * observe_spec["n_step"])
            )

    return observe_spec


def parse_update_spec(update_spec):
    """
    Parses update/learning parameters and inserts default values where necessary.

    Args:
        update_spec (Optional[dict]): Update/Learning spec dict.

    Returns:
        dict: The sanitized update_spec dict.
    """
    # If no spec given.
    default_spec = dict(
        # Whether to perform calls to `Agent.update()` at all.
        do_updates=True,
        # The unit in which we measure frequency: one of "timesteps", "episodes", "sec".
        # unit="timesteps", # TODO: not supporting any other than timesteps
        # The number of 'units' to wait before we do any updating at all.
        steps_before_update=0,
        # The frequency with which we update (given in `unit`).
        update_interval=4,
        # The number of consecutive `Agent.update()` calls per update.
        update_steps=1,
        # The batch size with which to update (e.g. when pulling records from a memory).
        batch_size=64,
        sync_interval=128
    )
    update_spec = default_dict(update_spec, default_spec)

    return update_spec
