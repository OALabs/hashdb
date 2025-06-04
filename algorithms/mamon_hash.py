#!/usr/bin/env python
DESCRIPTION = "Custom hash used in mamon ransomware"
TYPE = 'unsigned_int'
TEST_1 = 3726794573 

def hash(data):
    hash_value = 0x42

    for b in data:
        hash_value = ((hash_value * 33) + b) & 0xFFFFFFFF  # Keep it 32-bit

    return hash_value
