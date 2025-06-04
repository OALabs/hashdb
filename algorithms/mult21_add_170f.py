DESCRIPTION = "MULTIPLY 21 and ADD (0x170F base)"
TYPE = 'unsigned_int'
TEST_1 = 4233774810


def hash(data):
    hash_value = 0x170F
    for byte in data:
        hash_value = (hash_value * 0x21 + byte) & 0xFFFFFFFF
    return hash_value
