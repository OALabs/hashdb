#!/usr/bin/env python

DESCRIPTION = "shift+add with a custom initial value seen in a malware."
TYPE = "unsigned_int"
TEST_1 = 4294890437


def hash(data):
    result = 0x733e14f
    for val in data:
        result = (result << 1) + val
        result &= 0xffffffff
    return result
