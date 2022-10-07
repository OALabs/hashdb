#!/usr/bin/env python

DESCRIPTION = """
Danabot API hashing algorithm.

Reference: https://malwareandstuff.com/deobfuscating-danabots-api-hashing/
"""
TYPE = 'unsigned_int'
TEST_1 = 41476489


def hash(data):
    hash_val = 0

    i = 0
    data_len = len(data)
    while i < data_len:
        begin_chr = data[i]
        begin_chr_upper = ord(chr(begin_chr).upper())

        if i == data_len - 1:
            end_chr = data[0]
        else:
            end_chr = data[data_len - i - 2]
        end_chr_upper = ord(chr(end_chr).upper())

        v16 = (begin_chr ^ data_len) & 0xffffffff
        v18 = (end_chr ^ data_len) & 0xffffffff
        v17 = (begin_chr_upper ^ data_len) & 0xffffffff
        v15 = (end_chr_upper ^ data_len) & 0xffffffff

        hash_val = (v15 ^ (hash_val + v17 * v18 * v16)) & 0xffffffff

        i += 1

    return hash_val
