#!/usr/bin/env python

DESCRIPTION = "Guloader hash with seed 0x1505 and XOR 0x3C389ABC"
TYPE = 'unsigned_int'
TEST_1 = 2819429408


def hash(data):
    out_hash = 0x1505
    for c in data:
        out_hash = ((c + 33 * out_hash) ^ 0x3C389ABC) & 0xffffffff
    return out_hash
