#!/usr/bin/env python

DESCRIPTION = "API hash find in an unknown Mythic agent, need a XOR key"
# Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
TYPE = "unsigned_int"
# Test must match the exact has of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 3762100525


def hash(data):
    crc = 0xffffffff
    for val in data:
        for _ in range(8):
            tmp = crc
            crc = crc >> 1 & 0xffffffff
            if (val ^ tmp) & 1 != 0:
                crc ^= 0xedb88320
            val = val >> 1 & 0xffffffff
    return crc
