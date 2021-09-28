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

import stackhpc_monasca_agent_plugins.detection.nvidia_vgpu as nvidia_vgpu

input_args = {
    "username": "test"
}


class MockNvidiaVgpuDetectPlugin(nvidia_vgpu.NvidiaVgpuDetect):
    def __init__(self):
        self.args = input_args


class TestNvidiaVgpuDetect(unittest.TestCase):
    def setUp(self):
        self.nvidiavgpu = MockNvidiaVgpuDetectPlugin()

    def test_build_config(self):
        default_args = [
            'cache_dir',
            'nova_refresh',
            'metadata'
        ]
        config = self.nvidiavgpu.build_config()
        self.assertIn('nvidia_vgpu', config)
        init_config = config['nvidia_vgpu'].get('init_config')
        for item in default_args:
            self.assertIn(item, init_config)
        for item in input_args:
            self.assertIn(item, init_config)
