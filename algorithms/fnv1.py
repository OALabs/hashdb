#!/usr/bin/env python
DESCRIPTION = "FNV1 hash"
TYPE = 'unsigned_int'
TEST_1 = 3157003241


def hash(data):
    val = 0x811c9dc5
    for c in data:
        val = ((0x1000193 * val) ^ c ) & 0xffffffff
    return val
