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

import logging

from rlgraph.graphs import MetaGraphBuilder
from rlgraph.utils.input_parsing import parse_saver_spec, parse_execution_spec
from rlgraph.utils.rlgraph_errors import RLGraphError
from rlgraph.utils.specifiable import Specifiable


class GraphExecutor(Specifiable):
    """
    A GraphExecutor manages local and distributed execution of graphs by encapsulating
    session management, distributed optimization and communication.
    """
    def __init__(
        self,
        graph_builder,
        saver_spec=None,
        execution_spec=None,
        load_from_file=None
    ):
        """
        Abstract graph executor.
        Args:
            graph_builder (GraphBuilder): A graph builder which manages the RLGraph metagraph.
            saver_spec (dict): The saver specification for saving this graph to disk.
            execution_spec (dict): The specification dict for the execution types (local vs distributed, etc..) and
                settings (cluster types, etc..).
            load_from_file (Optional[bool,str]): If not None/False: Loads a previously stored checkpoint of the
                graph from an existing file. Thereby, supported values are:
                True: Use the latest checkpoint saved in `self.saver_spec["directory"]`.
                str: Use the given path/filename to load from.
        """
        super(GraphExecutor, self).__init__()

        self.logger = logging.getLogger(__name__)

        self.meta_graph_builder = MetaGraphBuilder()
        self.graph_builder = graph_builder

        self.saver_spec = parse_saver_spec(saver_spec)
        self.summary_spec = self.graph_builder.summary_spec
        self.execution_spec = parse_execution_spec(execution_spec)  # sanitize again (after Agent); one never knows

        # A global training/update counter. Should be increased by 1 each update/learning step.
        self.global_training_timestep = None

        self.logger.info("Execution spec is: {}".format(self.execution_spec))

        self.load_from_file = load_from_file

        self.seed = self.execution_spec.get("seed")

        # Default single-process execution.
        self.execution_mode = self.execution_spec.get("mode", "single")

        # Warning: If this is set to True, no automatic checkpointing or summary writing will be
        # performed because we will use a simple TensorFlow session instead of a monitored session.
        self.disable_monitoring = self.execution_spec.get("disable_monitoring", False)

        self.distributed_spec = self.execution_spec.get("distributed_spec")

        # Number of available GPUs and their names.
        self.gpus_enabled = None
        # Whether to fake GPUs in case there are none available (in which case, we place everything on the CPU).
        self.fake_gpus = None

        self.gpu_names = None
        self.used_devices = list()
        self.max_usable_gpus = 0
        self.num_gpus = 0

        self.device_strategy = None
        self.default_device = None
        self.device_map = None

    def build(self, root_components, input_spaces, **kwargs):
        """
        Sets up the computation graph by:
        - Starting the Server, if necessary.
        - Setting up the computation graph object.
        - Assembling the computation graph defined inside our root-component.
        - Setting up graph-savers, -summaries, and finalizing the graph.

        Args:
            root_components (list): List of root components where each root component corresponds to a
                meta graph to be built.
            input_spaces (dict): Dict with keys as core's API method names and values as tuples of Spaces that
                should go into these API methods.
        """
        raise NotImplementedError

    def execute(self, *api_method_calls):
        """
        Fetches one or more Socket outputs from the graph (given some api_methods) and returns their outputs.

        Args:
            api_method_calls (Union[str,list,tuple]): A specifier for an API-method call.
                - str: Call the API-method that has the given name w/o any input args.
                - tuple len=2: 0=the API-method name to call; 1=the input args to use for the call.
                - tuple len=3: same as len=2, AND 2=list of returned op slots to pull (e.g. [0]: only pull
                    the first op).

        Returns:
            any: The tuple of return values (or a single value) if only one API-method is called.
                The dictionary of result tuples (or single values) if more than one API-method is called.
        """
        raise NotImplementedError

    def read_variable_values(self, variables):
        """
        Read variable values from a graph, e.g. by calling the underlying graph
        or just returning the variable in imperative modes.

        Args:
            variables (list): Variable objects to retrieve from the graph.

        Returns:
            list: Values of the variables provided.
        """
        pass

    def init_execution(self):
        """
        Sets up backend-dependent execution, e.g. server for distributed TensorFlow
        execution.
        """
        pass  # not mandatory

    def finish_graph_setup(self):
        """
        Initializes any remaining backend-specific monitoring or session handling.
        """
        raise NotImplementedError

    def get_available_devices(self):
        """
        Lists available devices for this model.

        Returns:
            list: Device identifiers visible to this model.
        """
        pass

    def load_model(self, checkpoint_directory=None, checkpoint_path=None):
        """
        Loads model from specified path location using the following semantics:

        If checkpoint directory and checkpoint path are given, attempts to find `checkpoint_path` as relative path from
        `checkpoint_directory`.

        If a checkpoint directory is given but no path (e.g. because timestep of checkpoint is not known in advance),
        attempts to fetch latest check-point.

        If no directory is given, attempts to fetch checkpoint from the full absolute path `checkpoint_path'.

        Args:
            checkpoint_directory (str): Optional path to directory containing checkpoint(s).
            checkpoint_path (str): Path to specific model checkpoint.
        """
        raise NotImplementedError

    def store_model(self, path=None, add_timestep=True):
        """
        Saves the model to the given path (or to self.saver_directory). Optionally adds the current timestep
        to the filename to prevent overwriting previous checkpoint files.

        Args:
            path (str): The directory in which to save (default: self.saver_directory).
            add_timestep: Appends the current timestep to the checkpoint file if true.
        """
        raise NotImplementedError

    def get_device_assignments(self, device_names=None):
        """
        Get assignments for device(s).

        Args:
            device_names Optional(list):  Device names to filter for. If None, all assignments
                will be returned.

        Returns:
            dict: Dict mapping device identifiers (keys) to assigned components (list of component names).
        """
        pass

    #def get_weights(self):
    #    """
    #    Returns all weights for computation graph of this graph executor.

    #    Returns:
    #        any: Weights for this graph..
    #    """
    #    return self.execute("variables")

    #def set_weights(self, weights):
    #    """
    #    Sets weights of the underlying computation graph..

    #    Args:
    #        weights (any): Weights and optionally meta data to update depending on the backend.

    #    Raises:
    #        ValueError if weights do not match graph weights in shapes and types.
    #    """
    #    self.execute(("sync", weights))

    def terminate(self):
        """
        Terminates the GraphExecutor, so it will no longer be usable.
        Things that need to be cleaned up should be placed into this function, e.g. closing sessions
        and other open connections.
        """
        pass  # optional

    def sanity_check_component_tree(self, root_component):
        """
        Checks the initial component nesting setup (parent and their child components).

        Raises:
              RLGraphError: If sanity of the init nesting setup could not be confirmed.
        """
        # Check whether every component (except root-component) has a parent.
        components = root_component.get_all_sub_components(exclude_self=False)

        self.logger.info("Components created: {}".format(len(components)))

        core_found = False
        for component in components:
            if component.parent_component is None:
                if component is not root_component:
                    raise RLGraphError(
                        "ERROR: Component '{}' has no parent Component but is not the root-component! Only the "
                        "root-component has a `parent_component` of None.".format(component)
                    )
                else:
                    core_found = True
            elif component.parent_component is not None and component is root_component:
                raise RLGraphError(
                    "ERROR: Root-Component '{}' has a parent Component ({}), but is not allowed to!".
                    format(component, component.parent_component)
                )
        if core_found is False:
            raise RLGraphError("ERROR: Root-component '{}' was not found in meta-graph!".format(root_component))
