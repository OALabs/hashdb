#!/usr/bin/env python

DESCRIPTION = """

    Author = 0x0d4y

    Description = This new algorithm was discovered during ongoing monitoring of BabbleLoader, which implements it to obfuscate APIs.

    Sample_I    MD5: 06e1c0ee8a7f340d77c95be867c49284
    Sample_II   MD5: 7d1a15fd3c17ad226b3516bea26d7a94

    Reference: https://0x0d4y.blog/babbleloader-deep-dive-into-edr-and-machine-learning-based-endpoint-protection-evasion/

"""
TYPE = 'unsigned_int'

TEST_1 = 3847507269

def hash(data):
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    
    final_hash = 0
    for char in data:
        char_orded = ord(char)
        final_hash = (final_hash + char_orded) * (char_orded + 0x1c9943d2)
        final_hash &= 0xFFFFFFFF
    
    return final_hash

