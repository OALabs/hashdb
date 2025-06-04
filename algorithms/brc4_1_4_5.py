#!/usr/bin/env python

DESCRIPTION = "Hash algorithm used in BRC4 1.4.5"
# Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
TYPE = 'unsigned_int'
# Test must match the exact hash of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 3471553803


def hash(data):
    result = 0
    for c in data:
        temp = 2049 * result
        temp |= 0x2800000 
        temp += c
        result = temp & 0xFFFFFFFF
    
    return result
