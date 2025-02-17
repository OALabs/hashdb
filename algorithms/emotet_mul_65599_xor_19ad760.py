#!/usr/bin/env python

DESCRIPTION = """

    Author = rfLENtlr

    This algorithm was used by Emotet.

    Sample SHA256: 5d267403191a8786db2062584f298478ba59aa7b4d23adcf850a2c14a55c6d97

"""
TYPE = 'unsigned_int'
TEST_1 = 3163386495

def hash(data):
    hash_value = 0
    for c in data:
        hash_value = (c + hash_value * 0x1003f) & 0xFFFFFFFF
    return hash_value ^ 0x19ad760