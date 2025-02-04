#!/usr/bin/env python

DESCRIPTION = "OR 0x20 and XOR and ROL 19"
TYPE = 'unsigned_int'
TEST_1 = 0x186f3f38


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
    val = 0xffffffff
    ors = 0
    for i in data:
        ors = i | 32
        val = ors ^ rol(val, 19, 32)
    return val
