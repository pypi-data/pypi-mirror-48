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

import os

from setuptools import setup, find_packages

# Read __version__ avoiding imports that might be in install_requires.
version_vars = {}
with open(os.path.join(os.path.dirname(__file__), 'rlgraph', 'version.py')) as fp:
    exec(fp.read(), version_vars)

install_requires = [
    'absl-py',
    'numpy',
    'opencv-python',
    'packaging',  # Needed for version string comparisons.
    'pyyaml',
    'pytest',
    'requests',
    'scipy',
    'six'
]

setup_requires = []

extras_require = {
    # DL-backend specific extra-dependencies.
    'tf': ['tensorflow', 'tensorflow_probability'],
    'tf-gpu': ['tensorflow-gpu', 'tensorflow_probability'],
    'pytorch': ['torch', 'torchvision'],  # TODO platform dependent.
    'horovod': 'horovod',
    'ray': ['ray', 'lz4', 'pyarrow'],
    # Environment related extra dependencies.
    'gym': ['gym', 'atari-py'],  # To use openAI Gym Envs (e.g. Atari).
    'mlagents_env': ['mlagents'],  # To use MLAgents Envs (Unity3D).
    'pygame': ['pygame'],  # To use GridWorld Envs with visualization tools (not required).
    'graphviz': ['graphviz']  # To use GraphViz
}

setup(
    name='rlgraph',
    version=version_vars['__version__'],
    description='A Framework for Modular Deep Reinforcement Learning',
    long_description="""
RLgraph is a framework to quickly prototype, define and execute reinforcement learning
algorithms both in research and practice. RLgraph supports both
TensorFlow (or static graphs in general) and Pytorch (eager/define-by run execution) through
a single component based interface. An introductory blogpost can be found here: 
https://rlgraph.github.io/rlgraph/2019/01/04/introducing-rlgraph.html
""",
    url='https://rlgraph.org',
    author='The RLgraph development team',
    author_email='rlgraph@rlgraph.org',
    license='Apache 2.0',
    packages=[package for package in find_packages() if package.startswith('rlgraph')],
    install_requires=install_requires,
    setup_requires=setup_requires,
    extras_require=extras_require,
    zip_safe=False
)
