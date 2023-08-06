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


class RLGraphError(Exception):
    """
    Simple Error class.
    """
    pass


class RLGraphAPICallParamError(RLGraphError):
    """
    Raised if two sub-Components in a Stack do not have matching API-methods (sub-Component A's API output does not
    go well into sub-Component B's API input).
    """
    pass


class RLGraphBuildError(RLGraphError):
    """
    Raised if the build of a model cannot be completed properly e.g. due to input/variable-incompleteness of some
    components.
    """
    pass


class RLGraphInputIncompleteError(RLGraphError):
    """
    Raised if the build of a model cannot
    """
    def __init__(self, component, msg=None):
        """
        Args:
            component (Component): The Component that is not input complete.
            msg (Optional[str]): The error message.
        """
        msg = msg or "Component '{}' is input incomplete, but its input Spaces are needed in an API-call during the " \
                     "build procedure!".format(component.global_scope)
        super(RLGraphInputIncompleteError, self).__init__(msg)
        self.component = component


class RLGraphVariableIncompleteError(RLGraphError):
    """

    """
    def __init__(self, component, msg=None):
        """
        Args:
            component (Component): The Component that is not input complete.
            msg (Optional[str]): The error message.
        """
        msg = msg or "Component '{}' is variable incomplete, but its variables are needed in an API-call during the " \
                     "build procedure!".format(component.global_scope)
        super(RLGraphVariableIncompleteError, self).__init__(msg)
        self.component = component


class RLGraphObsoletedError(RLGraphError):
    """
    An error raised when some obsoleted method, property, etc. is used.
    """
    def __init__(self, type_, old_value, new_value):
        """
        Args:
            type_ (str): Some type description of what exactly is obsoleted.
            old_value (str): The obsoleted value used.
            new_value (str): The new (replacement) value that should have been used instead.
        """
        msg = "The {} '{}' you are using has been obsoleted! Use '{}' instead.".format(type_, old_value, new_value)
        super(RLGraphObsoletedError, self).__init__(msg)


class RLGraphSpaceError(RLGraphError):
    """
    A Space related error. Raises together with a message and Space information.
    """
    def __init__(self, space, msg=None):
        """
        Args:
            space (Space): The Space that failed some check.
            input_arg (Optional[str]): An optional API-method input arg name.
            msg (Optional[str]): The error message.
        """
        super(RLGraphSpaceError, self).__init__(msg)
        self.space = space


class RLGraphKerasStyleAssemblyError(RLGraphError):
    """
    Special error to raise when constructing a NeuralNetwork using our Keras-style assembly support.
    """
    pass
