#!/usr/bin/env python
########################################################################
# Copyright 2012 Mandiant
# Copyright 2014 FireEye
#
# Mandiant licenses this file to you under the Apache License, Version
# 2.0 (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.
#
# Reference:
# https://github.com/mandiant/flare-ida/blob/master/shellcode_hashes/make_sc_hash_db.py
#
########################################################################

DESCRIPTION = "FNV1 and XOR 67 observed in Neutrino Bot launcher"
TYPE = 'unsigned_int'
TEST_1 = 2949674906


def hash(data):
    val = 0x811c9dc5
    for c in data:
        val = (0x1000193 * (c ^ val)) & 0xffffffff
    return val ^ 0x67f
