#!/usr/bin/env python

DESCRIPTION = "A variant of the DJB2 hash algorithm that converts uppercase letters to lowercase"

TYPE = 'unsigned_int'

TEST_1 = 0xd87d4bef


def hash(data):
    hash_value = 0x624
    for char in data:
        if 0x41 <= char <= 0x5A:
            char += 0x20
        hash_value = (hash_value * 33 + char) & 0xFFFFFFFF
    return hash_value
