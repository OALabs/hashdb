#!/usr/bin/env python

DESCRIPTION = "ROR 13 and ADD with negative seed"
TYPE = 'unsigned_int'
TEST_1 = 2879724788


def ROR4(val, r_bits, max_bits):
    return ((val & (2**max_bits - 1)) >> r_bits % max_bits) | (val << (max_bits - (r_bits % max_bits)) & (2**max_bits - 1))


def hash(data):
    val = 0xffffffff
    for i in data:
        val = ROR4(val, 0xd, 32)
        val += i
    return val
