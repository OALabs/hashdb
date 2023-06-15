DESCRIPTION = 'API Hashing as used by d0nut'

TYPE = 'unsigned_int'
TEST_1 = 2349756695

rol = lambda val, r_bits, max_bits: \
    (val << r_bits % max_bits) & (2 ** max_bits-1) | \
    ((val & (2 ** max_bits-1)) >> (max_bits-(r_bits % max_bits)))


def hash(data):
    hashcalc = 75569

    for pointer in range(0, len(data), 4):
        if len(data) - pointer < 4:
            break
        shift_calc = data[pointer+0] | (data[pointer+1] << 8) | (data[pointer+2] << 16) | data[pointer+3] << 24
        hashcalc = (5 * rol(hashcalc ^ (0x27D4EB4F * ((0xE5438000 * shift_calc) | ((0x85EBCA87 * shift_calc & 0xFFFFFFFF) >> 17))), 13, 32))-1640531463 & 0xFFFFFFFF
    else:
        pointer = len(data)
    remainder = len(data) - pointer

    if remainder:
        remainder_bytes = int.from_bytes(data[-remainder:], 'little')
    else:
        remainder_bytes = 0

    rem_or = (0x27D4EB4F * ((0xE5438000 * remainder_bytes & 0xFFFFFFFF) | ((0x85EBCA87 * remainder_bytes & 0xFFFFFFFF) >> 17))) & 0xFFFFFFFF ^ (hashcalc ^ len(data))

    rem_hash = (0x165667C5 * ((0xC2B2AE63 * (rem_or ^ (rem_or >> 16)) & 0xFFFFFFFF) ^ ((0xC2B2AE63 * (rem_or ^ (rem_or >> 16)) & 0xFFFFFFFF) >> 13)) & 0xFFFFFFFF)
    rem_hash = rem_hash ^ (rem_hash >> 16)

    return rem_hash