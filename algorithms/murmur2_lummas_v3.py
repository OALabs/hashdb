#!/usr/bin/env python

DESCRIPTION = """
MurMurhash2 used in LummaStealer v3.0
seed 0x20
Reference: https://github.com/abrandoned/murmur2/blob/master/MurmurHash2.c"
"""

# Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
TYPE = 'unsigned_int'
# Test must match the exact hash of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 1874473983


def hash(data):
    seed = 0x20
    l = len(data)
    m = 0x5bd1e995
    h = seed ^ l

    x = l % 4
    o = l - x

    for i in range(0, o, 4):
        k = (data[i + 3] << 24) | (data[i + 2] << 16) | (data[i + 1] << 8) | data[i]
        k = (k * m) & 0xFFFFFFFF
        h = (((k ^ (k >> 24)) * m) ^ (h * m)) & 0xFFFFFFFF

    if x > 0:
        if x > 2:
            h ^= data[o + 2] << 16
        if x > 1:
            h ^= data[o + 1] << 8
        h = ((h ^ data[o]) * m) & 0xFFFFFFFF

    h = ((h ^ (h >> 13)) * m) & 0xFFFFFFFF
    return (h ^ (h >> 15)) & 0xFFFFFFFF