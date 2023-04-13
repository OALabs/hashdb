#!/usr/bin/env python

DESCRIPTION = "Seed 0x2326 shift right 1 shift left 7"
TYPE = 'unsigned_int'
TEST_1 = 0x9bfc4734


def hash(data):
    out = 0x2326
    for c in data:
        out = (out + c + ((out >> 1) | (out << 7))) & 0xffffffff
    return out
