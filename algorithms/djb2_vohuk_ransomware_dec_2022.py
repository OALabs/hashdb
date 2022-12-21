#!/usr/bin/env python

DESCRIPTION = "Vohuk Ransomware's variant of DJB2 as of December 2022"
TYPE = 'unsigned_int'
TEST_1 = 1274984080


def hash(data: bytearray) -> int:
    hash = 0x1505
    for b in data:
        if ((b - 0x41) & 0xFFFFFFFF) < 0x20:
            b += 0x20
        hash += b + ((0x20 * hash) & 0xFFFFFFFF)
        hash &= 0xFFFFFFFF
    return hash
