#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of datemike: https://github.com/angstwad/datemike
#
# Copyright 2014 Paul Durivage
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

from setuptools import setup
from datemike import __version__

setup(
    name='datemike',
    version=__version__,
    packages=['datemike'],
    url='https://github.com/angstwad/datemike',
    license='Apache v2.0',
    author='Paul Durivage',
    author_email='pauldurivage@gmail.com',
    description='Create Ansible tasks, plays, and playbooks in pure Python',
    install_requires=['pyyaml']
)
