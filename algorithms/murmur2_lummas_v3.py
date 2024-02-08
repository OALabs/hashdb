#!/usr/bin/env python

DESCRIPTION = """
MurMurhash2 used in LummaStealer v3.0
seed 0x20
Reference: https://github.com/abrandoned/murmur2/blob/master/MurmurHash2.c"
"""

# Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
TYPE = 'unsigned_int'
# Test must match the exact hash of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 1874473983


def hash(data):
    fun_len = len(data)
    seed = 0x20
    new_index = 0
    i = 0
    seeded_len = (fun_len ^ seed)
    if fun_len > 4:
        shifted_len = fun_len >> 2 & 0xFFFFFFFF
        fun_len = fun_len - (4 * (fun_len >> 2)) & 0xFFFFFFFF
        for i in range(0, len(data), 4):
            if shifted_len != 0:
                shifted_len = shifted_len - 1
                seeded_len = (seeded_len * 0x5BD1E995) & 0xFFFFFFFF
                ecx = ((((((data[i+3] << 8) | data[i+2]) << 8) | data[i+1]) << 8 | data[i]) * 0x5BD1E995) & 0xFFFFFFFF
                eax = ecx
                eax = eax >> 0x18 & 0xFFFFFFFF
                eax = (eax ^ ecx) & 0xFFFFFFFF
                ecx = (eax * 0x5BD1E995) & 0xFFFFFFFF
                seeded_len = (seeded_len ^ ecx) & 0xFFFFFFFF
            new_index = i
        if (fun_len - 1) == 0:
            eax = (data[new_index] ^ seeded_len) & 0xFFFFFFFF
            seeded_len = (eax * 0x5BD1E995) & 0xFFFFFFFF
            return eax
        elif (fun_len - 2) == 0:
            eax = (data[new_index+1] << 8) & 0xFFFFFFFF
            seeded_len = seeded_len ^ eax
            eax = data[new_index]
            eax = eax ^ seeded_len
            seeded_len = (eax * 0x5BD1E995) & 0xFFFFFFFF

        elif (fun_len - 3) != 0:
            pass
        else:
            eax = data[new_index+2]
            eax = eax << 0x10 & 0xFFFFFFFF
            seeded_len = (seeded_len ^ eax) & 0xFFFFFFFF
            eax = data[new_index+1]
            eax = (eax << 8) & 0xFFFFFFFF
            seeded_len = (seeded_len ^ eax) & 0xFFFFFFFF
            eax = data[new_index]
            eax = eax ^ seeded_len
            seeded_len = (eax * 0x5BD1E995) & 0xFFFFFFFF
        eax = seeded_len
        eax = eax >> 0xD & 0xFFFFFFFF
        eax = eax ^ seeded_len
        ecx = (eax * 0x5BD1E995) & 0xFFFFFFFF
        eax = ecx
        eax = (eax >> 0xF) & 0xFFFFFFFF
        eax = eax ^ ecx
        return eax
