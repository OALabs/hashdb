#!/usr/bin/env python

DESCRIPTION = """
    Author = 0x0d4y
    Description: This is the Hash algorithm that was implemented in the new version of Lockbit, Lockbit Green or Lockbit4.0, with the aim of resolving DLLs and APIs dynamically.
    Sample MD5: 15796971D60F9D71AD162060F0F76A02
    The value of the Hash contained in TEST_1, was the result of the string: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    Reference: https://0x0d4y.blog/lockbit4-0-evasion-tales/
"""
TYPE = 'unsigned_int'
TEST_1 = 3370265577  

def hash(data):
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    
    MASK_32BIT = 0xffffffff
    hash_value = 0x14bf
    char_index = 0

    for char in data:
        char_code = ord(char)
        
        if 0x41 <= char_code <= 0x5A:
            normalized_char = (char_code + 0x20) & MASK_32BIT
        else:
            normalized_char = char_code

        if char_index == 0:
            index_modifier = 0
        else:
            index_modifier = (char_index ^ 0x14bf) & MASK_32BIT

        hash_value = (index_modifier * (((char_index + 0x14bf) * normalized_char + (hash_value ^ normalized_char)) & MASK_32BIT) + normalized_char) & MASK_32BIT

        char_index += 1

    return hash_value