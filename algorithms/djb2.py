#!/usr/bin/env python

DESCRIPTION = "djb2 hash"
# Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
TYPE = 'unsigned_int'
# Test must match the exact has of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 205455184


def hash(data):
    generated_hash = 5381
    for b in data:
        generated_hash = (generated_hash * 33 + b) & 0xFFFFFFFF
    return generated_hash
