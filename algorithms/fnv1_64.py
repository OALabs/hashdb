#!/usr/bin/env python
DESCRIPTION = "FNV1 hash (64-bit)"
TYPE = 'unsigned_long'
TEST_1 = 10612290624328353880


def hash(data):
    val = 0xcbf29ce484222325
    for c in data:
        val = ((0x100000001b3 * val) ^ c) & 0xffffffffffffffff
    return val
