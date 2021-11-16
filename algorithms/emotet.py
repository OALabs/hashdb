#!/usr/bin/env python
DESCRIPTION = "Emotet November 2021"
TYPE = 'unsigned_int'
TEST_1 = 3172443423


def hash(data):
    hash_value = 0
    for i in range(len(data)):
        hash_value = (((hash_value << 16) & 0xffffffff)
                      + ((hash_value << 6) & 0xffffffff)
                      + data[i] - hash_value) & 0xffffffff
    return hash_value
