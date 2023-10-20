#!/usr/bin/env python
DESCRIPTION = "ADD 65599 and MULTIPLY"
TYPE = 'unsigned_int'
TEST_1 = 2480409887

def hash(data):
    result = 0
    for c in data:
        tmp = c + 32
        if(((c - ord('A')) & 0xFFFF) > 26):
            tmp = c
        result = (tmp + 0x1003F * result) & 0xFFFFFFFF
    
    return result
