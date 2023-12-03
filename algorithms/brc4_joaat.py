#!/usr/bin/env python

DESCRIPTION = "Jenkins One At A Time (JOAAT) Hashing Algorithm Used by BRC4"
# Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
TYPE = 'unsigned_int'
# Test must match the exact hash of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 4059668722


def hash(data):
    val = 0
    for c in data:
        v1 = ord(c) + val
        v2 = (1025 * v1) & 0xffffffff
        v3 = v2 >> 6
        val = v2 ^ v3

    val = (val + val * 8) & 0xffffffff
    r1 = val >> 11
    r2 = val ^ r1
    result = r2 * 32769 & 0xffffffff

    return result
