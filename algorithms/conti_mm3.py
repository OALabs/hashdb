'''
pymmh3 was written by Fredrik Kihlander and enhanced by Swapnil Gusani, and is placed in the public
domain. The authors hereby disclaim copyright to this source code.

pure python implementation of the murmur3 hash algorithm

https://code.google.com/p/smhasher/wiki/MurmurHash3

This was written for the times when you do not want to compile c-code and install modules,
and you only want a drop-in murmur3 implementation.

As this is purely python it is FAR from performant and if performance is anything that is needed
a proper c-module is suggested!

This module is written to have the same format as mmh3 python package found here for simple conversions:

https://pypi.python.org/pypi/mmh3/2.3.1
'''

DESCRIPTION = "Conti ransomware Murmur3 API hashing"
TYPE = 'unsigned_int'
TEST_1 = 1813940549

import sys as _sys
if (_sys.version_info > (3, 0)):
    def xrange( a, b, c ):
        return range( a, b, c )
    def xencode(x):
        if isinstance(x, bytes) or isinstance(x, bytearray):
            return x
        else:
            return x.encode()
else:
    def xencode(x):
        return x
del _sys


def hash( key ):
    seed = 0xe9ff0077
    ''' Implements 32bit murmur3 hash. '''

    key = bytearray( xencode(key.lower()) )

    def fmix( h ):
        h ^= h >> 16
        h  = ( h * 0x85ebca6b ) & 0xFFFFFFFF
        h ^= h >> 13
        h  = ( h * 0xc2b2ae35 ) & 0xFFFFFFFF
        h ^= h >> 16
        return h

    length = len( key )
    nblocks = int( length / 4 )

    h1 = seed

    c1 = 0xcc9e2d51
    c2 = 0x1b873593

    # body
    for block_start in xrange( 0, nblocks * 4, 4 ):
        # ??? big endian?
        k1 = key[ block_start + 3 ] << 24 | \
             key[ block_start + 2 ] << 16 | \
             key[ block_start + 1 ] <<  8 | \
             key[ block_start + 0 ]
             
        k1 = ( c1 * k1 ) & 0xFFFFFFFF
        k1 = ( k1 << 15 | k1 >> 17 ) & 0xFFFFFFFF # inlined ROTL32
        k1 = ( c2 * k1 ) & 0xFFFFFFFF
        
        h1 ^= k1
        h1  = ( h1 << 13 | h1 >> 19 ) & 0xFFFFFFFF # inlined ROTL32
        h1  = ( h1 * 5 + 0xe6546b64 ) & 0xFFFFFFFF

    # tail
    tail_index = nblocks * 4
    k1 = 0
    tail_size = length & 3

    if tail_size >= 3:
        k1 ^= key[ tail_index + 2 ] << 16
    if tail_size >= 2:
        k1 ^= key[ tail_index + 1 ] << 8
    if tail_size >= 1:
        k1 ^= key[ tail_index + 0 ]
    
    if tail_size > 0:
        k1  = ( k1 * c1 ) & 0xFFFFFFFF
        k1  = ( k1 << 15 | k1 >> 17 ) & 0xFFFFFFFF # inlined ROTL32
        k1  = ( k1 * c2 ) & 0xFFFFFFFF
        h1 ^= k1

    #finalization
    unsigned_val = fmix( h1 ^ length )
    return unsigned_val
    if unsigned_val & 0x80000000 == 0:
        return unsigned_val
    else:
        return -( (unsigned_val ^ 0xFFFFFFFF) + 1 )


