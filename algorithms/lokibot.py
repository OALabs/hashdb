#!/usr/bin/env python

DESCRIPTION = """
    Author= IlFranz

    This algorithm was used by Loki/LokiBot for API hashing

    Sample SHA256: 75af30d10a4a60bb1b260a0f4f9e3410448bd81328737678937145aa88eee108
"""
TYPE = 'unsigned_int'

TEST_1 = 4064566081


def hash(data):
    hash_value = 0xFFFFFFFF
    for char in data:
        hash_value ^= char
        for _ in range(8):
            if hash_value & 1:
                hash_value ^= 0x4358AD54
            hash_value >>= 1
    return ~hash_value & 0xFFFFFFFF