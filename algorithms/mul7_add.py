#!/usr/bin/env python
########################################################################
# Copyright 2022 quangnh89
#
# Win32/Tinba API hashing algorithm.
#
# https://www.virustotal.com/gui/file/ce9483f6284903d8d76d60f1a96b3ade33c77ded0cac1d1c2dc8979879d6f91e
#
########################################################################

DESCRIPTION = """
MULTIPLY 7 and ADD.
Used in Darkside Win32/Tinba API hash."""
TYPE = 'unsigned_int'
TEST_1 = 2894658687


def hash(data):
    val = 0x0
    for i in data:
        val = (val * 0x7) & 0xFFFFFFFF
        val = (val + (i & 0xFF)) & 0xFFFFFFFF
    return val
