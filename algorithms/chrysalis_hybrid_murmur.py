DESCRIPTION = '''
    A hybrid hashing algorithm that processes short strings with a standard 
    iterative loop and switches to a parallelized four-accumulator strategy for 
    strings of 16 bytes or more. The intermediate result is finalized using a 
    modified MurmurHash3 avalanche mixer to produce the output.
'''
TYPE = 'unsigned_int'
TEST_1 = 3873075608

def rol4(value, count):
    """Rotate Left 32-bit"""
    count %= 32
    value &= 0xFFFFFFFF
    return ((value << count) | (value >> (32 - count))) & 0xFFFFFFFF

def ror4(value, count):
    """Rotate Right 32-bit"""
    count %= 32
    value &= 0xFFFFFFFF
    return ((value >> count) | (value << (32 - count))) & 0xFFFFFFFF

def hash(data):

    # Convert string to list of integer bytes
    if isinstance(data, str):
        data = [ord(c) for c in data]
    else:
        data = list(data)

    data_len = len(data)
    idx = 0
    seed = 0
    
    # ---------------------------------------------------------
    # Path 1: Long Strings (>= 16 chars)
    # ---------------------------------------------------------
    if data_len >= 0x10:
        accumulator_1 = 0x2D10317
        accumulator_2 = 0x64998966
        accumulator_3 = 0xDEADBEEF
        accumulator_4 = 0x4076453E
        
        # Process in blocks of 4 bytes
        while data_len >= 4:
            # Accumulator 1
            term = (0x9E3779B1 * accumulator_1) & 0xFFFFFFFF
            sub  = (0x3B5C4B9 * data[idx]) & 0xFFFFFFFF
            accumulator_1 = rol4((term - sub) & 0xFFFFFFFF, 13)
            
            # Accumulator 2
            term = (0x9E3779B1 * accumulator_2) & 0xFFFFFFFF
            sub  = (0x3B5C4B9 * data[idx + 1]) & 0xFFFFFFFF
            accumulator_2 = rol4((term - sub) & 0xFFFFFFFF, 13)
            
            # Accumulator 3
            term = (0x9E3779B1 * accumulator_3) & 0xFFFFFFFF
            sub  = (0x3B5C4B9 * data[idx + 2]) & 0xFFFFFFFF
            accumulator_3 = rol4((term - sub) & 0xFFFFFFFF, 13)
            
            # Accumulator 4
            v12  = data[idx + 3]
            term = (0x9E3779B1 * accumulator_4) & 0xFFFFFFFF
            sub  = (0x3B5C4B9 * v12) & 0xFFFFFFFF
            accumulator_4 = rol4((term - sub) & 0xFFFFFFFF, 13)
            
            idx += 4
            # CRITICAL: The C code decrements the length variable here.
            # This affects the loop condition for the "Tail Loop" below.
            data_len -= 4

        # Merge accumulators into v13
        v13 = (rol4(accumulator_1, 1) + 
               rol4(accumulator_2, 7) + 
               rol4(accumulator_3, 12) + 
               ror4(accumulator_4, 14)) & 0xFFFFFFFF
               
        # Calculate specific seed for long strings
        # seed = 0x842A6D03 - 0x61C8864F * v13
        mult_res = (0x61C8864F * v13) & 0xFFFFFFFF
        seed = (0x842A6D03 - mult_res) & 0xFFFFFFFF
        
    # ---------------------------------------------------------
    # Path 2: Short Strings (< 16 chars)
    # ---------------------------------------------------------
    else:
        seed = 0xF50426A0

    # ---------------------------------------------------------
    # Common Tail Loop
    # ---------------------------------------------------------
    # NOTE: If the "Long String" path was taken, 'idx' is now large (e.g., 16)
    # and 'data_len' is small (e.g., 2).
    # Since idx >= data_len, this loop is SKIPPED for long strings.
    # This loop ONLY runs fully for short strings.
    
    i = (idx + seed) & 0xFFFFFFFF
    
    while idx < data_len:
        v16 = data[idx]
        idx += 1
        
        # i = 0x9E3779B1 * __ROL4__(i + 0x165667B1 * v16, 11)
        term_inner = (i + (0x165667B1 * v16)) & 0xFFFFFFFF
        rotated = rol4(term_inner, 11)
        i = (0x9E3779B1 * rotated) & 0xFFFFFFFF

    # ---------------------------------------------------------
    # Final Mixing
    # ---------------------------------------------------------
    # Term 1: (0x85EBCA77 * (i ^ (i >> 15)))
    term1 = (0x85EBCA77 * (i ^ (i >> 15))) & 0xFFFFFFFF
    
    # Term 2: term1 ^ (term1 >> 13)
    term2 = term1 ^ (term1 >> 13)
    
    # Term 3: 0xC2B2AE3D * term2
    term3 = (0xC2B2AE3D * term2) & 0xFFFFFFFF
    
    # Final: term3 ^ (term3 >> 16)
    final_hash = term3 ^ (term3 >> 16)
    
    return final_hash