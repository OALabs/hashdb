# Created by Still Hsu <still@teamt5.org>

DESCRIPTION = "Hash with seed 0x1459 (5209)"
TYPE = 'unsigned_int'
TEST_1 = 1867215476


def hash(data):
    hash_val = 0x1459
    for c in data:
        hash_val = (hash_val * 9 + c) & 0xFFFFFFFF
    return hash_val
