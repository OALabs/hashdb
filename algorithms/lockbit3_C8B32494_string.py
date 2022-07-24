#!/usr/bin/env python

DESCRIPTION = """
Modified ROR13 add algo used in the Lockbit 3.0 with a seed of 0x0 
and a hard coded hash start of 0xC8B32494 this is for strings only

Reference: https://c3rb3ru5d3d53c.github.io/malware-blog/lockbit-v3-api-hashing/
"""
TYPE = 'unsigned_int'
TEST_1 = 1345844799


def ror(n, rotations=1, width=32):
    return (2**width-1) & (n >> rotations | n << (width-rotations))


def hash_algo(string, seed):
    result = 0xC8B32494 ^ seed
    string += b'\x00'
    for c in string:
        result = ror(result, rotations=0x0d, width=32)
        result = (result + c) & 0xffffffff
        if c == 0x00:
            break
    return result


def hash(data):
    seed = 0
    string_hash = hash_algo(data, seed)
    return string_hash
