#!/usr/bin/env python

DESCRIPTION = """
Metasploit ROR13 hash used in a lot of shellcode.
Reference https://github.com/rapid7/metasploit-framework/blob/master/external/source/shellcode/windows/x86/src/hash.py
"""
TYPE = 'unsigned_int'
TEST_1 = 4294967294
TEST_API_DATA_1 = 'K\x00E\x00R\x00N\x00E\x00L\x003\x002\x00.\x00D\x00L\x00L\x00\x00\x00LoadLibraryA\x00'
TEST_API_1 = 119961420


def ror(dword, bits):
    return (dword >> bits | dword << (32 - bits)) & 0xFFFFFFFF


def hash(data):
    if b'\x00\x00\x00' not in data:
        return 0xfffffffe
    module, api = data.split(b'\x00\x00\x00')
    module += b'\x00\x00\x00'
    module_hash = 0
    api_hash = 0
    for c in module:
        module_hash = ror(module_hash, 13)
        module_hash += c
    for c in api:
        api_hash = ror(api_hash, 13)
        api_hash += c
    h = module_hash + api_hash & 0xFFFFFFFF
    return h
