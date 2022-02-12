#!/usr/bin/env python
import mmh3

DESCRIPTION = "MurmurHash3"
TYPE = 'unsigned_int'
TEST_1 = 0xa27af39b


def hash(data):
    return mmh3.hash(data, signed=False)
