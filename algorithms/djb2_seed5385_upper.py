#!/usr/bin/env python
DESCRIPTION = "DJB2 variant with seed 5385 and uppercase normalization"
TYPE = 'unsigned_int'
TEST_1 = 2671650580


def hash(data):
    """Compute the API hash from byte input.
    Returns a 32-bit unsigned int.
    """
    if isinstance(data, str):
        data = data.encode('utf-8')

    h = 5385
    for b in data:
        c = b
        if c > 96:  # lowercase -> uppercase for ASCII
            c -= 32
        h = (h * 33 + c) & 0xFFFFFFFF
    return h
