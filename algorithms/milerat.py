# Created by Still Hsu <still@teamt5.org>

DESCRIPTION = "Hashing algorithm used by MileRAT."
TYPE = 'unsigned_int'
TEST_1 = 150583839

def hash(data):
    esi = 0
    for c in data:
        esi = (c + 0x83 * esi) & 0xffffffff
    return (esi & 0x7fffffff)