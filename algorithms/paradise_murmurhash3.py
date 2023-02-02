#!/usr/bin/env python

DESCRIPTION = "Paradise ransomware implementation of MurmurHash3 with custom seed (0xDEADC0DE) - adapted from https://github.com/wc-duck/pymmh3"
# Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
TYPE = 'unsigned_int'
# Test must match the exact has of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 1653390361


def hash(data):

    import sys as _sys
    if (_sys.version_info > (3, 0)):
        def xrange(a, b, c):
            return range(a, b, c)

        def xencode(x):
            if isinstance(x, bytes) or isinstance(x, bytearray):
                return x
            else:
                return x.encode()
    else:

        def xencode(x):
            return x
    del _sys

    data = bytearray(xencode(data))

    def fmix(h):
        h ^= h >> 16
        h = (h * 0x85ebca6b) & 0xFFFFFFFF
        h ^= h >> 13
        h = (h * 0xc2b2ae35) & 0xFFFFFFFF
        h ^= h >> 16
        return h

    length = len(data)
    nblocks = int(length / 4)

    seed = 0xDEADC0DE
    h1 = seed

    c1 = 0xcc9e2d51
    c2 = 0x1b873593

    # body
    for block_start in xrange(0, nblocks * 4, 4):
        # ??? big endian?
        k1 = data[block_start + 3] << 24 | \
             data[block_start + 2] << 16 | \
             data[block_start + 1] << 8 | \
             data[block_start + 0]

        k1 = (c1 * k1) & 0xFFFFFFFF
        k1 = (k1 << 15 | k1 >> 17) & 0xFFFFFFFF  # inlined ROTL32
        k1 = (c2 * k1) & 0xFFFFFFFF

        h1 ^= k1
        h1 = (h1 << 13 | h1 >> 19) & 0xFFFFFFFF  # inlined ROTL32
        h1 = (h1 * 5 + 0xe6546b64) & 0xFFFFFFFF

    # tail
    tail_index = nblocks * 4
    k1 = 0
    tail_size = length & 3

    if tail_size >= 3:
        k1 ^= data[tail_index + 2] << 16
    if tail_size >= 2:
        k1 ^= data[tail_index + 1] << 8
    if tail_size >= 1:
        k1 ^= data[tail_index + 0]

    if tail_size > 0:
        k1 = (k1 * c1) & 0xFFFFFFFF
        k1 = (k1 << 15 | k1 >> 17) & 0xFFFFFFFF  # inlined ROTL32
        k1 = (k1 * c2) & 0xFFFFFFFF
        h1 ^= k1

    unsigned_val = fmix(h1 ^ length)
    return unsigned_val
