#!/usr/bin/env python

DESCRIPTION = "MULTIPLY 0x21 and ADD (seed 8952), used in PikaBot in February 2024"
# Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
TYPE = 'unsigned_int'
# Test must match the exact hash of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 0xDD4DE543


def hash(data):
    h = 8952
    for c in data:
        if c > 96:
            c -= 0x20
        h = (c + 0x21*h) & 0xFFFFFFFF
    return h
