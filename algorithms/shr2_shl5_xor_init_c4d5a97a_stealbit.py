#!/usr/bin/env python

DESCRIPTION = "SHIFT RIGHT 2 and SHIFT LEFT 5 and XOR with initialization constant 0xc4d5a97a used in Stealbit malware."
# Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
TYPE = 'unsigned_int'
# Test must match the exact has of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 4099635895


def hash(data):

    # Initialize the hash value to 0xc4d5a97a
    func_hash = 0xc4d5a97a

    # Iterate through input string bytes and update the
    # hash value
    for b in data:
        func_hash ^= ((func_hash >> 2) + ((func_hash << 5) + b)) & 0xFFFFFFFF

    return func_hash
