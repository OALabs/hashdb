#!/usr/bin/env python

DESCRIPTION = "Graphical Proton string hashing algorithm"
TYPE = 'unsigned_int'
TEST_1 = "2194288283"

ROTATE_BITMASK = {
    8  : 0xff,
    16 : 0xffff,
    32 : 0xffffffff,
    64 : 0xffffffffffffffff,
}

def ror(inVal, numShifts, dataSize=32):
    '''rotate right instruction emulation'''
    if numShifts == 0:
        return inVal
    if (numShifts < 0) or (numShifts > dataSize):
        raise ValueError('Bad numShifts')
    if (dataSize != 8) and (dataSize != 16) and (dataSize != 32) and (dataSize != 64):
        raise ValueError('Bad dataSize')
    bitMask = ROTATE_BITMASK[dataSize]
    return bitMask & ((inVal >> numShifts) | (inVal << (dataSize-numShifts)))

def hash(data):
        out = 0x3ddfb511
        for c in data:
            temp = ror(out, 8)
            out = (ord(c) + temp) ^ out
        return out
