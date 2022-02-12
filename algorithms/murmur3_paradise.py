#!/usr/bin/env python
import mmh3

DESCRIPTION = "MurmurHash3 used in Paradise malware with the seed: 0xDEADC0DE"
TYPE = 'unsigned_int'
TEST_1 = 0x628cbc19


def hash(data):
    return mmh3.hash(data, 0xDEADC0DE, signed=False)
