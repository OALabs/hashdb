#!/usr/bin/env python
DESCRIPTION = "FNV1a hash (64-bit)"
TYPE = 'unsigned_long'
TEST_1 = 14074705352429455374


def hash(data):
    val = 0xcbf29ce484222325
    for c in data:
        val = (0x100000001b3 * (c ^ val)) & 0xffffffffffffffff
    return val
