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

DESCRIPTION = "XOR and ROL 8 and SLICE hex"
TYPE = 'unsigned_int'
TEST_1 = 377121536


ROTATE_BITMASK = {
    8: 0xff,
    16: 0xffff,
    32: 0xffffffff,
    64: 0xffffffffffffffff,
}


def rol(inVal, numShifts, dataSize=32):
    '''rotate left instruction emulation'''
    if numShifts == 0:
        return inVal
    if (numShifts < 0) or (numShifts > dataSize):
        raise ValueError('Bad numShifts')
    if (dataSize != 8) and (dataSize != 16) and (dataSize != 32) and (dataSize != 64):
        raise ValueError('Bad dataSize')
    bitMask = ROTATE_BITMASK[dataSize]
    return bitMask & ((inVal << numShifts) | (inVal >> (dataSize-numShifts)))


def hash(data):
    val = 0
    for i in data:
        val = val ^ (i * 256)
        val = rol(val, 0x8, 32)
        val_hex = "%08x" % val
        valh_str = val_hex[4:6]
        valh = int(valh_str, 16)
        val = val ^ valh
    return val
