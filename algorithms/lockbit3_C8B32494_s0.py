#!/usr/bin/env python

DESCRIPTION = """
Modified ROR13 add algo used in the Lockbit 3.0 with a seed of 0x0 
and a hard coded hash start of 0xC8B32494

Reference: https://c3rb3ru5d3d53c.github.io/malware-blog/lockbit-v3-api-hashing/
"""
TYPE = 'unsigned_int'
TEST_1 = 4294967294
TEST_API_DATA_1 = b'kernel32.dllFindFirstFileExW'
TEST_API_1 = 0xaae0cefb ^ 0x29009fe6


def ror(n, rotations=1, width=32):
    return (2**width-1) & (n >> rotations | n << (width-rotations))


def hash_algo(string, seed):
    string = string + b'\x00'
    result = 0xC8B32494 ^ seed
    for c in string:
        result = ror(result, rotations=0x0d, width=32)
        result = (result + c) & 0xffffffff
        if c == 0x00:
            break
    return result


def hash(data):
    # This selects for only the wordlist in hashdb with
    # the format <dllname>_<apiname>
    if len(data.split(b'.dll')) != 2:
        return 0xfffffffe
    dll_name, api_name = data.split(b'.dll')
    dll_name = dll_name + b'.dll'
    print(f"dll: {dll_name}, api: {api_name}")
    seed = 0
    dll_hash = hash_algo(dll_name, seed)
    tmp_hash = hash_algo(api_name, dll_hash)
    return ~tmp_hash & 0xffffffff
