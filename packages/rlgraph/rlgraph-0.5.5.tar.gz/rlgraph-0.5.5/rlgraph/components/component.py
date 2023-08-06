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

import copy
import inspect
import re
import uuid
from collections import OrderedDict

import numpy as np
from six.moves import xrange as range_
from rlgraph import get_backend
from rlgraph.utils import util
from rlgraph.utils.decorators import rlgraph_api, component_api_registry, component_graph_fn_registry, \
    define_api_method, define_graph_fn
from rlgraph.utils.ops import DataOpDict, FLAT_TUPLE_OPEN, FLAT_TUPLE_CLOSE, TraceContext
from rlgraph.utils.rlgraph_errors import RLGraphError, RLGraphObsoletedError
from rlgraph.utils.specifiable import Specifiable

if get_backend() == "tf":
    import tensorflow as tf
elif get_backend() == "tf-eager":
    import tensorflow as tf
    import tensorflow.contrib.eager as eager
elif get_backend() == "pytorch":
    from rlgraph.utils import PyTorchVariable
    import torch


class Component(Specifiable):
    """
    Base class for a graph component (such as a layer, an entire function approximator, a memory, an optimizers, etc..).

    A component can contain other components and/or its own graph-logic (e.g. tf ops).
    A component's sub-components are connected to each other via in- and out-Sockets (similar to LEGO blocks
    and deepmind's sonnet).

    This base class implements the interface to add sub-components, create connections between
    different sub-components and between a sub-component and this one and between this component
    and an external component.

    A component also has a variable registry, the ability to save the component's structure and variable-values to disk,
    and supports adding its graph_fns to the overall computation graph.
    """
    call_count = 0

    # List of tuples (method_name, runtime)
    call_times = []

    def __init__(self, *sub_components, **kwargs):
        """
        Args:
            sub_components (Component): Specification dicts for sub-Components to be added to this one.

        Keyword Args:
            name (str): The name of this Component. Names of sub-components within a containing component
                must be unique. Names are used to label exposed Sockets of the containing component.
                If name is empty, use scope as name (as last resort).
            scope (str): The scope of this Component for naming variables in the Graph.
            device (str): Device this component will be assigned to. If None, defaults to CPU.
            trainable (Optional[bool]): Whether to make the variables of this Component always trainable or not.
                Use None for no specific preference.

            # TODO: remove when we have numpy-based Components (then we can do test calls to infer everything automatically)
            graph_fn_num_outputs (dict): A dict specifying which graph_fns have how many return values.
                This can be useful if graph_fns don't clearly have a fixed number of return values and the auto-inferral
                utility function cannot determine the actual number of returned values.

            switched_off_apis (Optional[Set[str]]): Set of API-method names that should NOT be build for this Component.
            
            backend (str): The custom backend that this Component obliges to. None to use the RLGraph global backend.
                Default: None.
            
            space_agnostic (bool): Whether this component does not care about input spaces (e.g. if it does not
                create any space-dependent variables). Default: False.

            nesting_level (Optional[int]): The Component's nesting level. Root component has 0.
                None for non-placed Components. Default: None.
        """
        super(Component, self).__init__()

        # Scope if used to create scope hierarchies inside the Graph.
        # self.logger = logging.getLogger(__name__)
        self.scope = kwargs.pop("scope", "")

        assert re.match(r'^[\w\-.]*$', self.scope), \
            "ERROR: scope {} does not match scope-pattern! Needs to be \\w or '-'.".format(self.scope)
        # The global scope string defining the exact nested position of this Component in the Graph.
        # e.g. "/core/component1/sub-component-a"
        self.global_scope = self.scope

        # Shared variable scope.
        self.reuse_variable_scope = kwargs.pop("reuse_variable_scope", None)

        # Names of sub-components that exist (parallelly) inside a containing component must be unique.
        self.name = kwargs.pop("name", self.scope)  # if no name given, use scope
        self.device = kwargs.pop("device", None)
        self.trainable = kwargs.pop("trainable", None)
        self.graph_fn_num_outputs = kwargs.pop("graph_fn_num_outputs", dict())
        self.switched_off_apis = kwargs.pop("switched_off_apis", set())
        self.backend = kwargs.pop("backend", None)
        self.space_agnostic = kwargs.pop("space_agnostic", None)
        self.nesting_level = kwargs.pop("nesting_level", None)

        assert not kwargs, "ERROR: kwargs ({}) still contains items!".format(kwargs)

        # Keep track of whether this Component has already been added to another Component and throw error
        # if this is done twice. Each Component can only be added once to a parent Component.
        self.parent_component = None  # type: Component

        # Dict of sub-components that live inside this one (key=sub-component's scope).
        self.sub_components = OrderedDict()

        # Link to the GraphBuilder object.
        self.graph_builder = None

        # `self.api_methods`: Dict holding information about which op-record-tuples go via which API
        # methods into this Component and come out of it.
        # keys=API method name; values=APIMethodRecord
        self.api_methods = {}

        # Maps names to callable API functions for eager calls.
        self.api_fn_by_name = {}
        # Maps names of methods to synthetically defined methods.
        self.synthetic_methods = set()

        # How this component executes its 'call' method.
        self.execution_mode = "static_graph" if self.backend != "python" else "define_by_run"

        # `self.api_method_inputs`: Registry for all unique API-method input parameter names and their Spaces.
        # Two API-methods may share the same input if their input parameters have the same names.
        # keys=input parameter name; values=Space that goes into that parameter
        self.api_method_inputs = {}
        # Registry for graph_fn records (only populated at build time when the graph_fns are actually called).
        self.graph_fns = {}
        self.register_api_methods_and_graph_fns()

        # Set of op-rec-columns going into a graph_fn of this Component and not having 0 op-records.
        # Helps during the build procedure to call these right away after the Component is input-complete.
        self.no_input_graph_fn_columns = set()
        # Set of op-records that are constant and thus can be processed right away at the beginning of the build
        # procedure.
        self.constant_op_records = set()
        # Whether we know already all our API-methods' call args' spaces.
        self.input_complete = False
        # Short-circuit-set to True, if no variables are generated by this Component anyway.
        if re.search(r'\spass\n$', inspect.getsource(self.create_variables)) and \
                re.search(r'\spass\n$', inspect.getsource(self.check_input_spaces)):
            self.input_complete = True

        # Whether all our sub-Components are input-complete. Only after that point, we can run our _variables graph_fn.
        self.variable_complete = False
        # Has this component been built yet by the graph builder?
        self.built = False

        # All Variables that are held by this component (and its sub-components) by name.
        # key=full-scope variable name (scope=component/sub-component scope)
        # value=the actual variable
        self.variable_registry = {}
        # All summary ops that are held by this component (and its sub-components) by name.
        # key=full-scope summary name (scope=component/sub-component scope)
        # value=the actual summary op
        self.summaries = {}
        # The regexp that a summary's full-scope name has to match in order for it to be generated and registered.
        # This will be set by the GraphBuilder at build time.
        self.summary_regexp = None

        # Now add all sub-Components (also support all sub-Components being given in a single list).
        sub_components = sub_components[0] if len(sub_components) == 1 and \
            isinstance(sub_components[0], (list, tuple)) else sub_components
        self.add_components(*sub_components)

    def register_api_methods_and_graph_fns(self):
        """
        Detects all methods of the Component that should be registered as API-methods for
        this Component and complements `self.api_methods` and `self.api_method_inputs`.
        Goes by the @api decorator before each API-method or graph_fn that should be
        auto-thin-wrapped by an API-method.
        """
        # Goes through the class hierarchy of `self` and tries to lookup all registered functions
        # (by name) that should be turned into API-methods.
        class_hierarchy = inspect.getmro(type(self))
        for class_ in class_hierarchy[:-2]:  # skip last two as its `Specifiable` and `object`
            api_method_recs = component_api_registry.get(class_.__name__)
            if api_method_recs is not None:
                for api_method_rec in api_method_recs:
                    if api_method_rec.name not in self.api_methods:
                        define_api_method(self, api_method_rec)
            graph_fn_recs = component_graph_fn_registry.get(class_.__name__)
            if graph_fn_recs is not None:
                for graph_fn_rec in graph_fn_recs:
                    if graph_fn_rec.name not in self.graph_fns:
                        define_graph_fn(self, graph_fn_rec)

    def get_number_of_allowed_inputs(self, api_method_name):
        """
        Returns the number of allowed input args for a given API-method.

        Args:
            api_method_name (str): The API-method to analyze.

        Returns:
            Tuple[int,int]: A tuple with the range (lower/upper bound) of allowed input args for the given API-method.
                An upper bound of None means that the API-method accepts any number of input args equal or larger
                than the lower bound.
        """
        input_names = self.api_methods[api_method_name].input_names
        num_allowed_inputs = [0, 0]
        for in_name in input_names:
            # Positional arg with default values (not required, only raise upper bound).
            if self.api_method_inputs[in_name] == "flex":
                num_allowed_inputs[1] += 1
            # Var-positional (no upper bound anymore).
            elif self.api_method_inputs[in_name] == "*flex":
                num_allowed_inputs[1] = None
            # Required arg (raise both lower and upper bound).
            else:
                num_allowed_inputs[0] += 1
                num_allowed_inputs[1] += 1

        return tuple(num_allowed_inputs)

    def check_input_completeness(self):
        """
        Checks whether this Component is "input-complete" and stores the result in self.input_complete.
        Input-completeness is reached (only once and then it stays that way) if all API-methods of this component
        (whose `must_be_complete` field is not set to False) have all their input Spaces defined.

        Also, if no variables are generated by this Component anyway, the component is input-complete.

        Returns:
            bool: Whether this Component is input-complete or not.
        """
        if self.input_complete is True:
            return True

        self.input_complete = True
        # Loop through all API methods.
        for method_name, api_method_rec in self.api_methods.items():
            # This API method doesn't have to be completed, ignore and don't add it to space_dict.
            if api_method_rec.must_be_complete is False:
                continue

            # Loop through all of this API-method's input parameter names and check, whether they
            # all have a Space defined.
            for input_name in api_method_rec.input_names:
                assert input_name in self.api_method_inputs
                # This one is not defined yet -> Component is not input-complete.
                if self.api_method_inputs[input_name] is None:
                    self.input_complete = False
                    self.logger.debug("Found incomplete input_name {} for method {}.".format(input_name, method_name))
                    return False
                # API-method has a var-positional parameter (*args): Check whether it has been called at
                # least once (in which case we have Space information stored under "args[0]").
                elif self.api_method_inputs[input_name] == "*flex":
                    # Check all keys "input_name[n]" for any None. If one None found -> input incomplete.
                    idx = 0
                    while True:
                        key = input_name+"["+str(idx)+"]"
                        if key not in self.api_method_inputs:
                            # We require at least one param if the flex param is the only param. Otherwise, none are ok.
                            if idx > (0 if len(api_method_rec.input_names) == 1 else -1):
                                break
                            # No input defined (has not been called) -> Not input complete.
                            else:
                                self.input_complete = False
                                self.logger.debug(
                                    "Found incomplete flex key {} for method {}.".format(key, method_name))

                                return False
                        elif self.api_method_inputs[key] is None:
                            self.input_complete = False
                            self.logger.debug(
                                "Found incomplete flex key {} for method {}.".format(key, method_name))
                            return False
                        idx += 1
                # API-method has **kwargs parameters: Check whether it has been called at
                # least once (in which case we have Space information stored under "kwargs['some key']").
                elif self.api_method_inputs[input_name] == "**flex":
                    keys = [k for k in self.api_method_inputs if re.match(r'{}\['.format(input_name), k)]
                    # Check all keys "input_name[n]" for any None. If one None found -> input incomplete.
                    for key in keys:
                        if self.api_method_inputs[key] is None:
                            self.logger.debug(
                                "Found incomplete kwargs key {} for method {}.".format(key, method_name))
                            self.input_complete = False
                            return False
        return True

    def check_variable_completeness(self):
        """
        Checks, whether this Component is input-complete AND all our sub-Components are input-complete.
        At that point, all variables are defined and we can run the `variables` graph_fn.

        Returns:
            bool: Whether this Component is "variables-complete".
        """
        # We are already variable-complete -> shortcut return here.
        if self.variable_complete is True:
            return True
        # We are not input-complete yet (our own variables have not been created) -> return False.
        elif self.input_complete is False:
            return False

        # Simply check all direct sub-Components for variable-completeness.
        for direct_child in self.sub_components.values():
            if re.search(r'^\.helper-', direct_child.scope):
                continue
            if not direct_child.check_variable_completeness():
                return False
        self.variable_complete = True
        return self.variable_complete

    def when_input_complete(self, input_spaces=None, action_space=None, device=None, summary_regexp=None):
        """
        Wrapper that calls both `self.check_input_spaces` and `self.create_variables` in sequence and passes
        the dict with the input_spaces for each argument (key=arg name) and the action_space as parameter.

        Args:
            input_spaces (Optional[Dict[str,Space]]): A dict with Space/shape information.
                keys=in-argument name (str); values=the associated Space.
                Use None to take `self.api_method_inputs` instead.

            action_space (Optional[Space]): The action Space of the Agent/GraphBuilder. Can be used to construct and connect
                more Components (which rely on this information). This eliminates the need to pass the action Space
                information into many Components' constructors.

            device (str): The device to use for the variables generated.

            summary_regexp (Optional[str]): A regexp (str) that defines, which summaries should be generated
                and registered.
        """
        # Store the summary_regexp to use.
        self.summary_regexp = summary_regexp
        # print("Completing with input spaces api arg = ", input_spaces)
        input_spaces = input_spaces or self.api_method_inputs
        # print("Completing with input spaces after lookup = ", input_spaces)

        # Allow the Component to check its input Space and catch input-space errors.
        self.check_input_spaces(input_spaces, action_space)

        # Allow the Component to create all its variables.
        if get_backend() == "tf":
            # TODO: write custom scope generator for devices (in case None, etc..).
            if device is not None:
                with tf.device(device):
                    if self.reuse_variable_scope:
                        with tf.variable_scope(name_or_scope=self.reuse_variable_scope, reuse=tf.AUTO_REUSE):
                            self.create_variables(input_spaces, action_space)
                    else:
                        with tf.variable_scope(self.global_scope):
                            self.create_variables(input_spaces, action_space)
            else:
                if self.reuse_variable_scope:
                    with tf.variable_scope(name_or_scope=self.reuse_variable_scope, reuse=tf.AUTO_REUSE):
                        self.create_variables(input_spaces, action_space)
                else:
                    with tf.variable_scope(self.global_scope):
                        self.create_variables(input_spaces, action_space)

        elif get_backend() == "pytorch":
            # No scoping/devices here, handled at tensor level.
            self.create_variables(input_spaces, action_space)
        # Add all created variables up the parent/container hierarchy.
        self.propagate_variables()

        self.built = True

    def check_input_spaces(self, input_spaces, action_space=None):
        """
        Should check on the nature of all in-Sockets Spaces of this Component. This method is called automatically
        by the Model when all these Spaces are know during the Model's build time.

        Args:
            input_spaces (Dict[str,Space]): A dict with Space/shape information.
                keys=in-Socket name (str); values=the associated Space
            action_space (Optional[Space]): The action Space of the Agent/GraphBuilder. Can be used to construct and
                connect more Components (which rely on this information). This eliminates the need to pass the
                action Space information into many Components' constructors.
        """
        pass

    def create_variables(self, input_spaces, action_space=None):
        """
        Should create all variables that are needed within this component,
        unless a variable is only needed inside a single _graph_fn-method, in which case,
        it should be created there.
        Variables must be created via the backend-agnostic self.get_variable-method.

        Note that for different scopes in which this component is being used, variables will not(!) be shared.

        Args:
            input_spaces (Dict[str,Space]): A dict with Space/shape information.
                keys=in-Socket name (str); values=the associated Space
            action_space (Optional[Space]): The action Space of the Agent/GraphBuilder. Can be used to construct and
                connect more Components (which rely on this information). This eliminates the need to pass the action
                Space information into many Components' constructors.
        """
        pass

    def register_variables(self, *variables):
        """
        Adds already created Variables to our registry. This could be useful if the variables are not created
        by our own `self.get_variable` method, but by some backend-specific object (e.g. tf.layers).
        Also auto-creates summaries (regulated by `self.summary_regexp`) for the given variables.

        Args:
            # TODO check if we warp PytorchVariable
            variables (Union[PyTorchVariable, SingleDataOp]): The Variable objects to register.
        """
        for var in variables:
            # Use our global_scope plus the var's name without anything in between.
            # e.g. var.name = "dense-layer/dense/kernel:0" -> key = "dense-layer/kernel"
            # key = re.sub(r'({}).*?([\w\-.]+):\d+$'.format(self.global_scope), r'\1/\2', var.name)
            key = re.sub(r':\d+$', "", var.name)
            # Already registered: Must be the same (shared) variable.
            if key in self.variable_registry:
                assert self.variable_registry[key] is var,\
                    "ERROR: Key '{}' in {}.variables already exists, but holds a different variable " \
                    "({} vs {})!".format(key, self.global_scope, self.variable_registry[key], var)
            # New variable: Register.
            else:
                self.variable_registry[key] = var
                # Auto-create the summary for the variable.
                scope_to_use = self.reuse_variable_scope or self.global_scope
                summary_name = var.name[len(scope_to_use) + (1 if scope_to_use else 0):]
                summary_name = re.sub(r':\d+$', "", summary_name)
                self.create_summary(summary_name, var)

    def get_variable(self, name="", shape=None, dtype="float", initializer=None, trainable=True,
                     from_space=None, add_batch_rank=False, add_time_rank=False, time_major=False, flatten=False,
                     local=False, use_resource=False):
        """
        Generates or returns a variable to use in the selected backend.
        The generated variable is automatically registered in this component's (and all parent components')
        variable-registry under its global-scoped name.

        Args:
            name (str): The name under which the variable is registered in this component.

            shape (Optional[tuple]): The shape of the variable. Default: empty tuple.

            dtype (Union[str,type]): The dtype (as string) of this variable.

            initializer (Optional[any]): Initializer for this variable.

            trainable (bool): Whether this variable should be trainable. This will be overwritten, if the Component
                has its own `trainable` property set to either True or False.

            from_space (Optional[Space,str]): Whether to create this variable from a Space object
                (shape and dtype are not needed then).

            add_batch_rank (Optional[bool,int]): If True and `from_space` is given, will add a 0th (1st) rank (None) to
                the created variable. If it is an int, will add that int instead of None.
                Default: False.

            add_time_rank (Optional[bool,int]): If True and `from_space` is given, will add a 1st (0th) rank (None) to
                the created variable. If it is an int, will add that int instead of None.
                Default: False.

            time_major (bool): Only relevant if both `add_batch_rank` and `add_time_rank` are True.
                Will make the time-rank the 0th rank and the batch-rank the 1st rank.
                Otherwise, batch-rank will be 0th and time-rank will be 1st.
                Default: False.

            flatten (bool): Whether to produce a FlattenedDataOp with auto-keys.

            local (bool): Whether the variable must not be shared across the network.
                Default: False.

            use_resource (bool): Whether to use the new tf resource-type variables.
                Default: False.

        Returns:
            DataOp: The actual variable (dependent on the backend) or - if from
                a ContainerSpace - a FlattenedDataOp or ContainerDataOp depending on the Space.
        """

        # Overwrite the given trainable parameter, iff self.trainable is actually defined as a bool.
        trainable = self.trainable if self.trainable is not None else (trainable if trainable is not None else True)

        # Called as getter.
        if shape is None and initializer is None and from_space is None:
            if name not in self.variable_registry:
                raise KeyError(
                    "Variable with name '{}' not found in registry of Component '{}'!".format(name, self.name)
                )
            # TODO: Maybe try both the pure name AND the name with global-scope in front.
            return self.variable_registry[name]

        # Called as setter.
        var = None

        # We are creating the variable using a Space as template.
        if from_space is not None:
            var = self._variable_from_space(
                flatten, from_space, name, add_batch_rank, add_time_rank, time_major, trainable, initializer, local,
                use_resource
            )

        # TODO: Revise possible arg combinations, move in utils.
        elif self.backend == "python" or get_backend() == "python" or get_backend() == "pytorch":
            if add_batch_rank is not False and isinstance(add_batch_rank, int):
                if isinstance(add_time_rank, int):
                    if time_major:
                        var = [[initializer for _ in range_(add_batch_rank)] for _ in range_(add_time_rank)]
                    else:
                        var = [[initializer for _ in range_(add_time_rank)] for _ in range_(add_batch_rank)]
                else:
                    var = [initializer for _ in range_(add_batch_rank)]
            elif add_time_rank is not False and isinstance(add_time_rank, int):
                var = [initializer for _ in range_(add_time_rank)]
            elif initializer is not None:
                # Return
                var = initializer
            elif shape is not None:
                # Use python list if possible:
                if len(shape) == 1:
                    if dtype == int:
                        var = [0 for _ in range(shape[0])]
                    elif dtype == float:
                        var = [0.0 for _ in range(shape[0])]
                else:
                    if dtype == int:
                        var = np.zeros(shape, dtype=np.int32)
                    elif dtype == float:
                        var = np.zeros(shape, dtype=np.float32)
            else:
                var = []

        # Direct variable creation (using the backend).
        elif get_backend() == "tf":
            # Provide a shape, if initializer is not given or it is an actual Initializer object (rather than an array
            # of fixed values, for which we then don't need a shape as it comes with one).
            if initializer is None or isinstance(initializer, tf.keras.initializers.Initializer):
                shape = tuple((() if add_batch_rank is False else
                               (None,) if add_batch_rank is True else (add_batch_rank,)) + (shape or ()))
            # Numpyize initializer and give it correct dtype.
            else:
                shape = None
                initializer = np.asarray(initializer, dtype=util.convert_dtype(dtype, "np"))

            var = tf.get_variable(
                name=name, shape=shape, dtype=util.convert_dtype(dtype), initializer=initializer, trainable=trainable,
                collections=[tf.GraphKeys.GLOBAL_VARIABLES if local is False else tf.GraphKeys.LOCAL_VARIABLES],
                use_resource=use_resource
            )
        elif get_backend() == "tf-eager":
            shape = tuple(
                (() if add_batch_rank is False else (None,) if add_batch_rank is True else (add_batch_rank,)) +
                (shape or ())
            )

            var = eager.Variable(
                name=name, shape=shape, dtype=util.convert_dtype(dtype), initializer=initializer, trainable=trainable,
                collections=[tf.GraphKeys.GLOBAL_VARIABLES if local is False else tf.GraphKeys.LOCAL_VARIABLES]
            )

        # TODO: what about python variables?
        # Registers the new variable with this Component.
        key = ((self.reuse_variable_scope + "/") if self.reuse_variable_scope else
               (self.global_scope + "/") if self.global_scope else "") + name
        # Container-var: Save individual Variables.
        # TODO: What about a var from Tuple space?
        if isinstance(var, OrderedDict):
            for sub_key, v in var.items():
                self.variable_registry[key + sub_key] = v
        else:
            self.variable_registry[key] = var

        return var

    def _variable_from_space(self, flatten, from_space, name, add_batch_rank, add_time_rank, time_major, trainable,
                             initializer, local=False, use_resource=False):
        """
        Private variable from space helper, see 'get_variable' for API.
        """
        # Variables should be returned in a flattened OrderedDict.
        # TODO can we hide this tf.variable_scope somewhere?
        if get_backend() == "tf":
            if self.reuse_variable_scope is not None:
                with tf.variable_scope(name_or_scope=self.reuse_variable_scope, reuse=True):
                    if flatten:
                        return from_space.flatten(mapping=lambda key_, primitive: primitive.get_variable(
                            name=name + key_, add_batch_rank=add_batch_rank, add_time_rank=add_time_rank,
                            time_major=time_major, trainable=trainable, initializer=initializer,
                            is_python=(self.backend == "python" or get_backend() == "python"),
                            local=local, use_resource=use_resource
                        ))
                    # Normal, nested Variables from a Space (container or primitive).
                    else:
                        return from_space.get_variable(
                            name=name, add_batch_rank=add_batch_rank, trainable=trainable, initializer=initializer,
                            is_python=(self.backend == "python" or get_backend() == "python"),
                            local=local, use_resource=use_resource
                        )
            else:
                if flatten:
                    return from_space.flatten(mapping=lambda key_, primitive: primitive.get_variable(
                        name=name + key_, add_batch_rank=add_batch_rank, add_time_rank=add_time_rank,
                        time_major=time_major, trainable=trainable, initializer=initializer,
                        is_python=(self.backend == "python" or get_backend() == "python"),
                        local=local, use_resource=use_resource
                    ))
                # Normal, nested Variables from a Space (container or primitive).
                else:
                    return from_space.get_variable(
                        name=name, add_batch_rank=add_batch_rank, trainable=trainable, initializer=initializer,
                        is_python=(self.backend == "python" or get_backend() == "python"),
                        local=local, use_resource=use_resource
                    )

        elif get_backend() == "pytorch":
            if flatten:
                return from_space.flatten(mapping=lambda key_, primitive: primitive.get_variable(
                    name=name + key_, add_batch_rank=add_batch_rank, add_time_rank=add_time_rank,
                    time_major=time_major, trainable=trainable, initializer=initializer,
                    is_python=True, local=local, use_resource=use_resource
                ))
            # Normal, nested Variables from a Space (container or primitive).
            else:
                return from_space.get_variable(
                    name=name, add_batch_rank=add_batch_rank, trainable=trainable, initializer=initializer,
                    is_python=True, local=local, use_resource=use_resource
                )

    def get_variables(self, *names, **kwargs):
        """
        Utility method to get one or more component variable(s) by name(s).

        Args:
            names (List[str]): Lookup name strings for variables. None for all.

        Keyword Args:
            collections (set): A set of collections to which the variables have to belong in order to be returned here.
                Default: tf.GraphKeys.TRAINABLE_VARIABLES
            custom_scope_separator (str): The separator to use in the returned dict for scopes.
                Default: '/'.
            global_scope (bool): Whether to use keys in the returned dict that include the global-scopes of the
                Variables. Default: False.
            get_ref (bool): Whether to return the ref or the value when using PyTorch. Default: False (return
                values).
        Returns:
            dict: A dict mapping variable names to their get_backend variables.
        """
        if get_backend() == "tf":
            collections = kwargs.pop("collections", None) or tf.GraphKeys.GLOBAL_VARIABLES
            custom_scope_separator = kwargs.pop("custom_scope_separator", "/")
            global_scope = kwargs.pop("global_scope", True)
            assert not kwargs, "{}".format(kwargs)

            if len(names) == 1 and isinstance(names[0], list):
                names = names[0]
            names = util.force_list(names)
            # Return all variables of this Component (for some collection).
            if len(names) == 0:
                collection_variables = tf.get_collection(collections)
                ret = {}
                for v in collection_variables:
                    lookup = re.sub(r':\d+$', "", v.name)
                    if lookup in self.variable_registry:
                        if global_scope:
                            # Replace the scope separator with a custom one.
                            ret[re.sub(r'(/|{}|{})'.format(FLAT_TUPLE_CLOSE, FLAT_TUPLE_OPEN),
                                       custom_scope_separator, lookup)] = v
                        else:
                            ret[re.sub(r'^.+/', "", lookup)] = v
                return ret
            # Return only variables of this Component by name.
            else:
                return self.get_variables_by_name(
                    *names, custom_scope_separator=custom_scope_separator, global_scope=global_scope
                )
        elif get_backend() == "pytorch":
            # There are no collections - just return variables for this component if names are empty.
            custom_scope_separator = kwargs.pop("custom_scope_separator", "/")
            global_scope = kwargs.pop("global_scope", True)
            get_ref = kwargs.pop("get_ref", False)

            if len(names) == 0:
                names = list(self.variable_registry.keys())
            return self.get_variables_by_name(
                *names, custom_scope_separator=custom_scope_separator, global_scope=global_scope,
                get_ref=get_ref
            )

    def get_variables_by_name(self, *names, **kwargs):
        """
        Retrieves this components variables by name.

        Args:
            names (List[str]): List of names of Variable to return.

        Keyword Args:
            custom_scope_separator (str): The separator to use in the returned dict for scopes.
                Default: '/'.
            global_scope (bool): Whether to use keys in the returned dict that include the global-scopes of the
                Variables. Default: False.
            get_ref (bool): Whether to return the ref or the value when using PyTorch. Default: False (return
                values).
        Returns:
            dict: Dict containing the requested names as keys and variables as values.
        """
        custom_scope_separator = kwargs.pop("custom_scope_separator", "/")
        global_scope = kwargs.pop("global_scope", False)
        get_ref = kwargs.pop("get_ref", False)
        assert not kwargs

        variables = {}
        if get_backend() == "tf":
            for name in names:
                global_scope_name = ((self.global_scope + "/") if self.global_scope else "") + name
                if name in self.variable_registry:
                    variables[re.sub(r'/', custom_scope_separator, name)] = self.variable_registry[name]
                elif global_scope_name in self.variable_registry:
                    if global_scope:
                        variables[re.sub(r'/', custom_scope_separator, global_scope_name)] = self.variable_registry[
                            global_scope_name]
                    else:
                        variables[name] = self.variable_registry[global_scope_name]
        elif get_backend() == "pytorch":
            # Unpack tuple.
            if isinstance(names, tuple) and len(names) == 1:
                names = names[0]
            # print("names = ", names)
            state = None
            if TraceContext.DEFINE_BY_RUN_CONTEXT == "execution" and hasattr(self, "get_state"):
                state = self.get_state()
            for name in names:
                global_scope_name = ((self.global_scope + "/") if self.global_scope else "") + name
                if state is not None:
                    # Generally using underscores in attribute names, not scope separates
                    lookup = name.replace("-", "_")
                    if lookup in state:
                        variables[name] = state[lookup]
                    elif name in state:
                        variables[name] = state[name]
                elif name in self.variable_registry:
                    if get_ref:
                        variables[re.sub(r'/', custom_scope_separator, name)] = self.variable_registry[name]
                    else:
                        variables[re.sub(r'/', custom_scope_separator, name)] = self.read_variable(self.variable_registry[name])
                elif global_scope_name in self.variable_registry:
                    if global_scope:
                        if get_ref:
                            variables[re.sub(r'/', custom_scope_separator, global_scope_name)] = \
                                self.variable_registry[global_scope_name]
                        else:
                            variables[re.sub(r'/', custom_scope_separator, global_scope_name)] = \
                                self.read_variable(self.variable_registry[global_scope_name])
                    else:
                        if get_ref:
                            variables[name] = self.variable_registry[global_scope_name]
                        else:
                            variables[name] = self.read_variable(self.variable_registry[global_scope_name])

        return variables

    def create_summary(self, name, values, summary_type="histogram"):
        """
        Creates a summary op (and adds it to the graph).
        Skips those, whose full name does not match `self.summary_regexp`.

        Args:
            name (str): The name for the summary. This has to match `self.summary_regexp`.
                The name should not contain a "summary"-prefix or any global scope information
                (both will be added automatically by this method).

            values (op): The op to summarize.

            summary_type (str): The summary type to create. Currently supported are:
                "histogram", "scalar" and "text".
        """
        # Prepend the "summaries/"-prefix.
        name = "summaries/" + name
        # Get global name.
        global_name = ((self.global_scope + "/") if self.global_scope else "") + name
        # Skip non matching summaries (all if summary_regexp is None).
        if self.summary_regexp is None or not re.search(self.summary_regexp, global_name):
            return

        summary = None
        if get_backend() == "tf":
            ctor = getattr(tf.summary, summary_type)
            summary = ctor(name, values)

        # Registers the new summary with this Component.
        if global_name in self.summaries:
            raise RLGraphError("ERROR: Summary with name '{}' already exists in {}'s summary "
                               "registry!".format(global_name, self.name))
        self.summaries[global_name] = summary
        self.propagate_summary(global_name)

    def propagate_summary(self, summary_key):
        """
        Propagates a single summary op of this Component to its parents' summaries registries.

        Args:
            summary_key (str): The lookup key for the summary to propagate.
        """
        # Return if there is no parent.
        if self.parent_component is None:
            return

        # If already there -> Error.
        if summary_key in self.parent_component.summaries:
            raise RLGraphError("ERROR: Summary registry of '{}' already has a summary under key '{}'!".
                               format(self.parent_component.name, summary_key))
        self.parent_component.summaries[summary_key] = self.summaries[summary_key]

        # Recurse up the container hierarchy.
        self.parent_component.propagate_summary(summary_key)

    def add_components(self, *components, expose_apis=None):
        """
        Adds sub-components to this one.

        Args:
            components (List[Component]): The list of Component objects to be added into this one.

            expose_apis (Optional[Set[str],Dict[str,str]]): An optional set of strings with API-methods of the child
                component that should be exposed as the parent's API via a simple wrapper API-method for the parent
                (that calls the child's API-method).
        """
        if expose_apis is None:
            expose_apis = {}
        elif isinstance(expose_apis, str):
            expose_apis = {expose_apis}

        for component in components:
            # Safety measure: Ignore Nones.
            if component is None:
                continue

            # Try to create Component from spec.
            if not isinstance(component, Component):
                component = Component.from_spec(component)
            # Make sure no two components with the same name are added to this one (own scope doesn't matter).
            if component.name in self.sub_components:
                raise RLGraphError("ERROR: Sub-Component with name '{}' already exists in '{}'!".
                                   format(component.name, self.global_scope))
            # Make sure each Component can only be added once to a parent/container Component.
            elif component.parent_component is not None:
                raise RLGraphError(
                    "ERROR: Sub-Component with name '{}' has already been added once to a containing Component! Each "
                    "Component can only be added once to a parent.".format(component.name)
                )
            # Make sure we don't add to ourselves.
            elif component is self:
                raise RLGraphError("ERROR: Cannot add a Component ({}) as a sub-Component to itself!".format(self.name))
            component.parent_component = self
            component.nesting_level = (self.nesting_level or 0) + 1
            component.graph_builder = self.graph_builder
            self.sub_components[component.name] = component

            # Fix the sub-component's (and sub-sub-component's etc..) scope(s).
            self.propagate_scope(component)

            # Execution modes must be coherent within one component subgraph.
            self.propagate_sub_component_properties(
                properties=dict(execution_mode=self.execution_mode, nesting_level=(self.nesting_level or 0) + 1),
                component=component
            )

            # Should we expose some API-methods of the child?
            # Only if parent does not have that method yet (otherwise, use parent method).
            for api_method_name, api_method_rec in component.api_methods.items():
                if api_method_name in expose_apis and api_method_name not in self.api_methods:
                    exposed_api_method_name = api_method_name if isinstance(expose_apis, set) else \
                        expose_apis[api_method_name]
                    # Build exposed method code per string, then eval it.
                    code = "@rlgraph_api(component=self, must_be_complete={}, ok_to_overwrite=False)\n".format(
                        api_method_rec.must_be_complete
                    )
                    code += "def {}(self, ".format(exposed_api_method_name)
                    args_str = ""
                    args_str_w_default = ""
                    for i, ak in enumerate(api_method_rec.non_args_kwargs):
                        args_str += ak + ", "
                        args_str_w_default += ak + ("="+str(api_method_rec.default_values[api_method_rec.default_args.index(ak)]) if ak in api_method_rec.default_args else "") + ", "
                    args_str += ("*"+api_method_rec.args_name+", " if api_method_rec.args_name else "")
                    args_str += ("**"+api_method_rec.kwargs_name+", " if api_method_rec.kwargs_name else "")
                    args_str = args_str[:-2]  # -2=cut last ', '
                    code += args_str_w_default[:-2] + "):\n" # -2=cut last ', '
                    code += "\treturn getattr(self.sub_components['{}'], '{}')({})\n".format(component.name, api_method_name, args_str)
                    print("Expose API {} from {} to {} code:\n".format(api_method_name, component.name, self.name) + code)
                    exec(code, globals(), locals())

        # Add own reusable scope to front of all sub-components' reusable scope.
        if self.reuse_variable_scope is not None:
            # Propagate reuse_variable_scope down to the added Component's sub-components.
            self.propagate_sub_component_properties(
                properties=dict(reuse_variable_scope=self.reuse_variable_scope)
            )

    def get_all_sub_components(self, list_=None, level_=0, exclude_self=False):
        """
        Returns all sub-Components (including self, unless `exclude_self` is True) sorted by their nesting-level
        (... grand-children before children before parents). If the nesting level is the same, sort alphabetically
        by the scope (name) of the Components.

        Args:
            list_ (Optional[List[Component]])): A list of already collected components to append to.
            level_ (int): The slot indicating the Component level depth in `list_` at which we are currently.
            exclude_self (bool): Whether `self` should be returned as the last sub-Component in the list.
                Default: True.

        Returns:
            List[Component]: A list with all the sub-components in `self` (and `self` itself if `exclude_self` is False).
        """
        return_ = False
        # This is the final-return recursive call-level.
        if list_ is None:
            list_ = {}
            return_ = True
        if level_ not in list_:
            list_[level_] = []
        list_[level_].append(self)
        level_ += 1
        for sub_component in self.sub_components.values():
            sub_component.get_all_sub_components(list_, level_)
        if return_:
            ret = []
            for l in sorted(list_.keys(), reverse=True):
                ret.extend(sorted(list_[l], key=lambda c: c.scope))
            if exclude_self:
                return ret[:-1]
            return ret

    def get_sub_component_by_global_scope(self, scope):
        """
        Returns a sub-Component (or None if not found) by scope. The sub-coponent's scope should be given
        as global scope of the sub-component (not local scope with respect to this Component).

        Args:
            scope (str): The global scope of the sub-Component we are looking for.

        Returns:
            Component: The sub-Component with the given global scope if found, None if not found.
        """
        # TODO: make method more efficient.
        components = self.get_all_sub_components(exclude_self=True)
        for component in components:
            if component.global_scope == scope:
                return component
        return None

    def get_sub_component_by_name(self, name):
        """
        Returns a sub-Component (or None if not found) by its name (local scope). The sub-Component must be a direct
        sub-Component of `self`.

        Args:
            name (str): The name (local scope) of the sub-Component we are looking for.

        Returns:
            Component: The sub-Component with the given name if found, None if not found.

        Raises:
            RLGraphError: If a sub-Component by that name could not be found.
        """
        sub_component = self.sub_components.get(name, None)
        if sub_component is None:
            raise RLGraphError("ERROR: sub-Component with name '{}' not found in '{}'!".format(name, self.global_scope))
        return sub_component

    def remove_sub_component_by_name(self, name):
        """
        Removes a sub-component from this one by its name. Thereby sets the `parent_component` property of the
        removed Component to None.
        Raises an error if the sub-component does not exist.

        Args:
            name (str): The name of the sub-component to be removed.

        Returns:
            Component: The removed component.
        """
        assert name in self.sub_components, "ERROR: Component {} cannot be removed because it is not" \
            "a sub-component. Sub-components by name are: {}.".format(name, list(self.sub_components.keys()))
        removed_component = self.sub_components.pop(name)
        # Set parent of the removed component to None.
        removed_component.parent_component = None
        return removed_component

    def get_parents(self):
        """
        Returns a list of parent and grand-parents of this component.

        Returns:
            List[Component]: A list (may be empty if this component has no parents) of all parent and grand-parents.
        """
        ret = []
        component = self
        while component.parent_component is not None:
            ret.append(component.parent_component)
            component = component.parent_component
        return ret

    def propagate_scope(self, sub_component):
        """
        Fixes all the sub-Component's (and its sub-Component's) global_scopes.

        Args:
            sub_component (Optional[Component]): The sub-Component object whose global_scope needs to be updated.
                Use None for this Component itself.
        """
        # TODO this should be moved to use generic method below, but checking if global scope if set
        # TODO does not work well within that.
        if sub_component is None:
            sub_component = self
        elif self.global_scope:
            sub_component.global_scope = self.global_scope + (
                ("/" + sub_component.scope) if sub_component.scope else "")

        # Recurse.
        for sc in sub_component.sub_components.values():
            sub_component.propagate_scope(sc)

    def propagate_sub_component_properties(self, properties, component=None, recursive_=False):
        """
        Recursively updates properties of component and its sub-components.

        Args:
            properties (dict): Dict with names of properties and their values to recursively update
                sub-components with.

            component (Optional([Component])): Component to recursively update. Uses self if None.

            recursive_ (bool): Whether this is a recursive (sub-Component) call. Default: False.
        """
        if component is None:
            component = self
        properties_scoped = copy.deepcopy(properties)
        for name, value in properties.items():
            # Property is some scope (value is then that scope of the parent component).
            # Have to align it with sub-component's local scope.
            if value and (name == "global_scope" or name == "reuse_variable_scope"):
                # For the parent component, do not add its scope to the shared-scope.
                if recursive_ is True:
                    value += (("/" + component.scope) if component.scope else "")
                properties_scoped[name] = value
                setattr(component, name, value)
            # Normal property: Set to static given value.
            else:
                setattr(component, name, value)
                # Nesting_level: Increase by one the deeper we go.
                if name == "nesting_level":
                    properties_scoped[name] = value + 1
        for sc in component.sub_components.values():
            component.propagate_sub_component_properties(properties_scoped, sc, recursive_=True)

    def propagate_variables(self, keys=None):
        """
        Propagates all variable from this Component to its parents' variable registries.

        Args:
            keys (Optional[List[str]]): An optional list of variable names to propagate. Should only be used in
                internal, recursive calls to this same method.
        """
        # Return if there is no parent.
        if self.parent_component is None:
            return

        # Add all our variables to parent's variable registry.
        keys = keys or self.variable_registry.keys()
        for key in keys:
            # If already there (bubbled up from some child component that was input complete before us)
            # -> Make sure the variable object is identical.
            if key in self.parent_component.variable_registry:
                if self.variable_registry[key] is not self.parent_component.variable_registry[key]:
                    raise RLGraphError("ERROR: Variable registry of '{}' already has a variable under key '{}'!". \
                          format(self.parent_component.name, key))
            self.parent_component.variable_registry[key] = self.variable_registry[key]

        # Recurse up the container hierarchy.
        self.parent_component.propagate_variables(keys)

    def copy(self, name=None, scope=None, device=None, trainable=None,
             reuse_variable_scope=None, reuse_variable_scope_for_sub_components=None):
        """
        Copies this component and returns a new component with possibly another name and another scope.
        The new component has its own variables (they are not shared with the variables of this component as they
        will be created after this copy anyway, during the build phase).
        and is initially not connected to any other component.

        Args:
            name (str): The name of the new Component. If None, use the value of scope.
            scope (str): The scope of the new Component. If None, use the same scope as this component.
            device (str): The device of the new Component. If None, use the same device as this one.

            trainable (Optional[bool]): Whether to make all variables in this component trainable or not. Use None
                for no specific preference.

            reuse_variable_scope (Optional[str]): If not None, variables of the copy will be shared under this scope.

            reuse_variable_scope_for_sub_components (Optional[str]): If not None, variables only of the sub-components
                of the copy will be shared under this scope.

        Returns:
            Component: The copied component object.
        """
        # Make sure we are still in the assembly phase (should not copy actual ops).
        assert self.built is False, "ERROR: Cannot copy a Component ('{}') that has already been built!". \
            format(self.name)

        if scope is None:
            scope = self.scope
        if name is None:
            name = scope
        if device is None:
            device = self.device
        if trainable is None:
            trainable = self.trainable

        # Remove the parent ref (will be set to None for the copy anyway).
        parent_ref = self.parent_component
        self.parent_component = None

        # Make sure, containing Agents are not copied either.
        agent_ref = None
        if hasattr(self, "agent"):
            agent_ref = self.agent
            self.agent = None

        # Simply deepcopy self and change name and scope.
        new_component = copy.deepcopy(self)
        new_component.name = name
        new_component.scope = scope
        # Change global_scope for the copy and all its sub-components.
        new_component.global_scope = scope
        new_component.propagate_scope(sub_component=None)

        # Propagate reusable scope, device and other trainable.
        new_component.propagate_sub_component_properties(
            properties=dict(device=device, trainable=trainable)
        )
        if reuse_variable_scope:
            new_component.propagate_sub_component_properties(dict(reuse_variable_scope=reuse_variable_scope))
        # Gives us the chance to skip new_component's scope.
        elif reuse_variable_scope_for_sub_components:
            for sc in new_component.sub_components.values():
                sc.propagate_sub_component_properties(dict(reuse_variable_scope=reuse_variable_scope_for_sub_components))

        # Put back critical refs.
        if agent_ref is not None:
            self.agent = new_component.agent = agent_ref
        # Leave the copy's parent_component at None.
        self.parent_component = parent_ref

        return new_component

    @staticmethod
    def scatter_update_variable(variable, indices, updates):
        """
        Updates a variable. Optionally returns the operation depending on the backend.

        Args:
            variable (any): Variable to update.
            indices (array): Indices to update.
            updates (any):  Update values.

        Returns:
            Optional[op]: The graph operation representing the update (or None).
        """
        if get_backend() == "tf":
            return tf.scatter_update(ref=variable, indices=indices, updates=updates)

    @staticmethod
    def assign_variable(ref, value):
        """
        Assigns a variable to a value.

        Args:
            ref (any): The variable to assign to.
            value (any): The value to use for the assignment.

        Returns:
            Optional[op]: None or the graph operation representing the assignment.
        """
        if get_backend() == "tf":
            tensor_type = type(value).__name__
            if tensor_type == "Variable" or tensor_type == "RefVariable":
                return tf.assign(ref=ref, value=value.read_value())
            else:
                return tf.assign(ref=ref, value=value)
        elif get_backend() == "pytorch":
            ref.set_value(value)

    @staticmethod
    def read_variable(variable, indices=None, dtype=None, shape=None):
        """
        Reads a variable.

        Args:
            variable (DataOp): The variable whose value to read.
            indices (Optional[np.ndarray,tf.Tensor]): Indices (if any) to fetch from the variable.
            dtype (Optional[torch.dtype]): Optional dtype to convert read values to.
            shape (Optional[tuple]): Optional default shape.

        Returns:
            any: Variable values.
        """
        if get_backend() == "tf":
            if indices is not None:
                # Could be redundant, question is if there may be special read operations
                # in other backends, or read from remote variable requiring extra args.
                return tf.gather(params=variable, indices=indices)
            else:
                return variable
        elif get_backend() == "pytorch":
            # PyTorchVariable is used to store torch parameters (e.g. layers).
            if isinstance(variable, PyTorchVariable):
                return variable.get_value()
            # Lists or numpy arrays may be used to store mutable state that does not need
            # tensor operations.
            elif isinstance(variable, list) or isinstance(variable, np.ndarray):
                if TraceContext.DEFINE_BY_RUN_CONTEXT == "building" \
                        and shape is not None and (indices is None or len(indices) == 0):
                    return torch.zeros(shape, dtype=dtype)

                if indices is not None:
                    ret = []
                    for i in indices:
                        val = variable[i]
                        # Type checking is necessary because torch.stack only works on same types.
                        if isinstance(val, torch.Tensor):
                            if dtype is None:
                                ret.append(val)
                            elif dtype == torch.float32:
                                ret.append(val.float())
                            elif dtype == torch.int32:
                                ret.append(val.int())
                            elif dtype == torch.uint8:
                                ret.append(val.byte())
                    # Stack list into one Tensor with a btach dim.
                    return torch.stack(ret) if ret else ret
                else:
                    return variable
            else:
                # Catch all for raw types.
                return variable

    def sub_component_by_name(self, scope_name):
        """
        Returns a sub-component of this component by its name.

        Args:
            scope_name (str): Name of the component. This is typically its scope.

        Returns:
            Component: Sub-component if it exists.

        Raises:
            ValueError: Error if no sub-component with this name exists.
        """
        if scope_name not in self.sub_components:
            raise RLGraphError(
                "Name {} is not a valid sub-component name for component {}. Sub-Components are: {}".
                format(scope_name, self.__str__(), self.sub_components.keys())
            )
        return self.sub_components[scope_name]

    def _post_build(self, component):
        component.post_define_by_run_build()
        for sub_component in component.sub_components.values():
            self._post_build(sub_component)

    def post_define_by_run_build(self):
        """
        Optionally execute post-build calls.
        """
        # Try resetting state.
        component_state = self.get_state()
        if component_state is not None:
            for name in component_state.keys():
                if hasattr(self, name) and isinstance(getattr(self, name), (float, int)):
                    self.__setattr__(name, 0)

    def get_state(self):
        """
        Optionally provide define-by-run state as dict.

        Returns:
            dict: Names and values of variables.
        """
        pass

    def get_helper_component(self, type_, *args, **kwargs):
        """
        Returns a helper component of the given type (only one helper component per type is allowed
        and necessary). If a helper of the type does not exist yet in `self`, create a new one.

        Args:
            type_ (str): The type as a string of the helper Component to return.

        Returns:
            Component: The helper component.
        """
        name = ".helper-"+type_+"-{}".format(uuid.uuid4())
        helper = self.sub_components.get(name)
        if helper is None:
            kwargs.update(dict(type=type_, scope=name))
            if len(args) > 0:
                kwargs.update({"_args": args})
            helper = Component.from_spec(kwargs)
            self.add_components(helper)
        return helper

    @rlgraph_api(returns=1, requires_variable_completeness=True)
    def _graph_fn_variables(self):
        """
        Outputs all of this Component's variables in a DataOpDict (API-method "variables").

        This can be used e.g. to sync this Component's variables into another Component, which owns
        a Synchronizable() as a sub-component. The returns values of this graph_fn are then sent into
        the other Component's API-method `sync` (parameter: "values") for syncing.

        Returns:
            DataOpDict: Dict with keys=variable names and values=variable (SingleDataOp).
        """
        # Must use custom_scope_separator here b/c RLGraph doesn't allow Dict with '/'-chars in the keys.
        # '/' could collide with a FlattenedDataOp's keys and mess up the un-flatten process.
        variables_dict = self.get_variables(custom_scope_separator="-")
        return DataOpDict(variables_dict)

    def _variables(self):
        """
        OBSOLETED API method. New "variables()" should be used.
        """
        raise RLGraphObsoletedError("API-method", "_variables()", "variables()")

    @staticmethod
    def reset_profile():
        """
        Sets profiling values to 0.
        """
        Component.call_count = 0
        Component.call_times = []

    def __str__(self):
        return "{}('{}' api={})".format(type(self).__name__, self.name, str(list(self.api_methods.keys())))
