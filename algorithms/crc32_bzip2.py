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

DESCRIPTION = "bzip2 version of crc32"
TYPE = 'unsigned_int'
TEST_1 = 2691965320


def hash(data):
    crc32_table = [0] * 256
    for i in range(256):
        v = i << 24
        for j in range(8):
            if (v & 0x80000000) == 0:
                v = (2 * v) & 0xffffffff
            else:
                v = ((2 * v) ^ 0x4C11DB7) & 0xffffffff
        crc32_table[i] = v
    result = 0xffffffff
    for c in data:
        result = (crc32_table[ c ^ ((result >> 24) & 0xff) ] ^ (result << 8)) & 0xffffffff
    return (result ^ 0xffffffff) & 0xffffffff
