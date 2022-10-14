#!/usr/bin/env python

DESCRIPTION = "Blister loader v2 api hash"
TYPE = 'unsigned_int'
TEST_1 = 0x6d223692


def hash(data):
    h = 0x78f1e5bf
    for c in data:
        h = (((c ^ h) & 0xffffffff) * 0x5bd1e995) & 0xffffffff
        h = (h ^ ((h >> 15) & 0xffffffff)) & 0xffffffff
    return h
