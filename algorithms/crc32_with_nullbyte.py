#!/usr/bin/env python

#Copyright by Max 'Libra' Kersten <https://maxkersten.nl>

import zlib

DESCRIPTION = "The CRC32 hash of the given string with the terminating null byte added to it. This algorithm is used in PlugX samples."
TYPE = 'unsigned_int'
TEST_1 = 3133185683

def hash(data):
    data = data + b'\x00'
    return 0xffffffff & zlib.crc32(data)
