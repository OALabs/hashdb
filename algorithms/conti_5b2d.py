#!/usr/bin/env python

DESCRIPTION = "Conti ransomware api hash with seed 0x5B2D"
TYPE = 'unsigned_int'
TEST_1 = 3350281850


def hash(data):
    API_buffer = []

    i = len(data) >> 3

    count = 0
    while i != 0:
        for index in range(0, 8):
            API_buffer.append(data[index + count])
        count += 8
        i -= 1

    if len(data) & 7 != 0:
        v8 = len(data) & 7

        while v8 != 0:
            API_buffer.append(data[count])
            count += 1
            v8 -= 1

    hash_val = 0

    for i in range(0, len(API_buffer)):
        API_buffer[i] = ord(chr(API_buffer[i]))

    v15 = 0x5B2D
    string_length_2 = len(data)
    API_buffer_count = 0
    if len(data) >= 4:
        count = string_length_2 >> 2
        string_length_2 = (string_length_2 - 4 *
                           (string_length_2 >> 2)) & 0xFFFFFFFF

        while True:
            temp_buffer_val = API_buffer[API_buffer_count +
                                         3] << 24 | API_buffer[API_buffer_count +
                                                               2] << 16 | API_buffer[API_buffer_count +
                                                                                     1] << 8 | API_buffer[API_buffer_count]

            temp = (0x5BD1E995 * temp_buffer_val) & 0xFFFFFFFF
            API_buffer_count += 4
            v15 = ((0x5BD1E995 * (temp ^
                                  (temp >> 0x18))) & 0xFFFFFFFF) ^ ((0x5BD1E995 * v15) & 0xFFFFFFFF)
            count -= 1
            if count == 0:
                break

    v18 = string_length_2 - 1

    v19 = v18 - 1

    if v18 == 0:
        hash_val ^= API_buffer[API_buffer_count]
    elif v19 == 0:
        hash_val ^= API_buffer[API_buffer_count + 1] << 8
        hash_val ^= API_buffer[API_buffer_count]
    elif v19 == 1:
        hash_val ^= API_buffer[API_buffer_count + 2] << 16
        hash_val ^= API_buffer[API_buffer_count + 1] << 8
        hash_val ^= API_buffer[API_buffer_count]

    v20 = (0x5BD1E995 * hash_val) & 0xFFFFFFFF
    edi = (0x5BD1E995 * len(data)) & 0xFFFFFFFF

    eax = v20 >> 0x18
    eax ^= v20

    ecx = (0x5BD1E995 * eax) & 0xFFFFFFFF
    eax = (0x5BD1E995 * v15) & 0xFFFFFFFF

    ecx ^= eax

    eax = edi
    eax >>= 0x18
    eax ^= edi

    edx = (0x5BD1E995 * ecx) & 0xFFFFFFFF
    eax = (0x5BD1E995 * eax) & 0xFFFFFFFF
    edx ^= eax
    eax = edx

    eax >>= 0xD
    eax ^= edx

    ecx = (0x5BD1E995 * eax) & 0xFFFFFFFF
    eax = ecx
    eax >>= 0xF
    eax ^= ecx

    return eax
