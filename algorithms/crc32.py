#!/usr/bin/env python
# -*- coding: utf-8 -*-

DESCRIPTION = "Standard crc32 hash."
TYPE = 'unsigned_int'
TEST_1 = 3632233996



import zlib

def get_hash(data):
    return 0xffffffff & zlib.crc32(data)

