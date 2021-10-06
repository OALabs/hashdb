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

DESCRIPTION = "Multiple permutations of 0xe8677835"
TYPE = 'unsigned_int'
TEST_1 = 3113210072


def hash(data):
    val = 0xFFFFFFFF
    for i in data:
        val ^= i
        for j in range(0, 8):
            if (val & 0x1) == 1:
                val ^= 0xe8677835
            val >>= 1
    return val ^ 0xFFFFFFFF
