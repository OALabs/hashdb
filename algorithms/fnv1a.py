#!/usr/bin/env python
DESCRIPTION = "FNV1a hash"
TYPE = 'unsigned_int'
TEST_1 = 2949673445


def hash(data):
    val = 0x811c9dc5
    for c in data:
        val = (0x1000193 * (c ^ val)) & 0xffffffff
    return val
