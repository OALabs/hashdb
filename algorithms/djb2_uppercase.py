#!/usr/bin/env python

DESCRIPTION = "A variant of the DJB2 hash algorithm that converts lowercase letters to uppercase"
TYPE = 'unsigned_int'
TEST_1 = 0x07AB31C2

def hash(data):
    hash_value = 4919
    for char in data:
        if isinstance(char, int):
            char = chr(char)
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        hash_value = (hash_value * 33) + ord(char)
    return hash_value & 0xFFFFFFFF
