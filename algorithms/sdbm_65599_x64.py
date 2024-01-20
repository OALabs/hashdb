DESCRIPTION = "The original SDBM hash function with the constant 65599. Used by Emotet malware."
TYPE = 'unsigned_long'
TEST_1 = 18326187587583583519


def hash(data):
    hsh = 0
    for d in data:
        hsh = d + 0x1003f * hsh
    return hsh & 0xffffffffffffffff
