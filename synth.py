# Copyright 2018 Google LLC
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

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
import synthtool.gcp as gcp
import logging
from pathlib import Path
import subprocess

logging.basicConfig(level=logging.DEBUG)

gapic = gcp.GAPICGenerator()
# create common templates by gapic
common_templates = gcp.CommonTemplates()

versions = ['v2', 'v2beta1']
for version in versions:
    library = gapic.node_library('dialogflow', version)

s.copy(library, excludes=['package.json', 'README.md'])

templates = common_templates.node_library(package_name="dialogflow")
s.copy(templates)

'''
Node.js specific cleanup
'''
subprocess.run(['npm', 'ci'])

subprocess.run(['npm', 'run', 'prettier'])
subprocess.run(['npm', 'run', 'lint'])
