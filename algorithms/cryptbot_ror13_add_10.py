# !/usr/bin/env python

DESCRIPTION = "Add 10 to ror13 shift on data"
TYPE = 'unsigned_int'
TEST_1 = 3425182094


rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def hash(data):


    GENERATED_HASH = 0
    for character in data:

        segment_1 = ror(GENERATED_HASH, 13, 32) & 0xffffffff
        segment_2 = character
        if segment_2 >= 97:
            segment_2 -= 32
        GENERATED_HASH = segment_1 + segment_2
    return GENERATED_HASH + 10

