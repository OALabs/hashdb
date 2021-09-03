#!/usr/bin/env python

DESCRIPTION = """
BlackMatter ransomware api hash from August 2021 using ror 13 and increment.
Reference hash: 22d7d67c3af10b1a37f277ebabe2d1eb4fd25afbd6437d4377400e148bcc08d6
"""
TYPE = 'unsigned_int'
TEST_1 = 3952613812


def ror(value, count=1, base=8):
    value = (value >> count | value << (base - count)) & (2**base - 1)
    return value


def hash(data):
    out = 0
    for i in data:
        out = (i + ror(out, count=13, base=32)) & 0xffffffff
    return out
