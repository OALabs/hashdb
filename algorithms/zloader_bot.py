#!/usr/bin/env python

DESCRIPTION = "API hashing used by the zloader bot on 2021-10-21"
# Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
TYPE = 'unsigned_int'
# Test must match the exact has of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 3694482793


def hash(data):
    generated_hash = 0
    for i in range(len(data)):
        current_char = data[i]
        v17 = (current_char + (generated_hash << 4)) & 0xFFFFFFFF
        if v17 & 0xF0000000 != 0:
            v10 = (v17 & 0xF0000000) >> 0x18
            v18 = v17 & 0xFFFFFFFF
            v11 = v18 ^ 0x0FFFFFFF
            generated_hash = (v18 & ~v10) | (v10 & v11)
        else:
            generated_hash = v17

    return generated_hash
