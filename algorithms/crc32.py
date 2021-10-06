#!/usr/bin/env python
import zlib

DESCRIPTION = "Standard crc32 hash."
TYPE = 'unsigned_int'
TEST_1 = 532866770


def hash(data):
    return 0xffffffff & zlib.crc32(data)
