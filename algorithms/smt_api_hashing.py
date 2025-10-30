#!/usr/bin/env python
import ctypes

DESCRIPTION = """

    Author = 0x0d4y

    Description = This is the API Hashing algorithm, of ScoringMathTea RAT used by Lazarus.

    Sample_I    MD5: cc9cf047aec871cefb1c7d4b8d5d3432

"""
TYPE = 'unsigned_int'
TEST_1 = 797271551

def hash(data):
    h = 0x2DBB955  # Seed value
    for char_byte in data:
        if char_byte >= 128:
            signed_char_val = char_byte - 256
        else:
            signed_char_val = char_byte

        signed_h = ctypes.c_int32(h).value
        
        s = signed_h >> 2
        m = signed_h * 32
        right_side = (signed_char_val + s + m)

        h = (h ^ right_side) & 0xFFFFFFFF
   
    return h