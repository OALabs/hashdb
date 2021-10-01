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

DESCRIPTION = "API hash routine unique to PoisonIvy RAT"
TYPE = 'unsigned_int'
TEST_1 = 3632233996


ROTATE_BITMASK = {
    8: 0xff,
    16: 0xffff,
    32: 0xffffffff,
    64: 0xffffffffffffffff,
}

def rcr(inVal, numShifts, cb, dataSize=32):
    '''rotate carry right instruction emulation'''
    if numShifts == 0:
        return inVal
    if (numShifts < 0) or (numShifts > dataSize):
        raise ValueError('Bad numShifts')
    #make sure carry in bit is only 0 or 1
    cb = cb & 1
    if (dataSize != 8) and (dataSize != 16) and (dataSize != 32) and (dataSize != 64):
        raise ValueError('Bad dataSize')
    #or the carry value in there
    bitMask = ROTATE_BITMASK[dataSize]
    inVal = inVal | (cb << dataSize)
    x = (dataSize - numShifts) + 1
    res = (inVal >> numShifts) | (inVal << x)
    return (bitMask & res, 1 & (res >> dataSize))


def hash(data):
    cx = 0xffff
    dx = 0xffff
    for b1 in data:
        bx = 0
        ax = b1 ^ (cx & 0xff)
        cx =  ((cx>>8)&0xff) | ((dx&0xff)<<8)
        dx = ((dx>>8)&0xff) | 0x800
        while (dx & 0xff00) != 0:
            c_in = bx & 1
            bx = bx >> 1          
            ax, c_out = rcr(ax, 1, c_in, 16)
            if c_out != 0:
                ax = ax ^ 0x8320
                bx = bx ^ 0xedb8
            dx =  (dx&0xff) | (((((dx>>8)&0xff)-1)&0xff)<<8)
        cx = cx ^ ax
        dx = dx ^ bx
    dx = 0xffff & ~dx
    cx = 0xffff & ~cx
    return  0xffffffff & ((dx<<16) | cx)
