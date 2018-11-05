# Copyright (c) 2018 StackHPC Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

import stackhpc_monasca_agent_plugins.detection.nvidia as nvidia


class MockNvidiaDetectPlugin(nvidia.NvidiaDetect):
    def __init__(self):
        # Don't call the base class constructor
        pass


class TestNvidiaDetect(unittest.TestCase):
    def setUp(self):
        self.nvidia = MockNvidiaDetectPlugin()

    def test_build_config(self):
        config = self.nvidia.build_config()
        self.assertIn('nvidia', config)
