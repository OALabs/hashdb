#!/usr/bin/env python

DESCRIPTION = "MULTIPLY 3 and ADD, starting key 0x9C"
TYPE = 'unsigned_int'
TEST_1 = 3481051867


def hash(data):
    key = 0x9C
    for byte in data:
        dword = byte & 0xffffffff
        key = (key * 3) & 0xffffffff
        key = (key + dword) & 0xffffffff
    return key
