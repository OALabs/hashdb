DESCRIPTION = "MurmurHash3 with seed 0x93fb64"
TYPE = 'unsigned_int'
# Test must match the exact hash of the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 0x2113849f

SEED = 0x93fb64

def murmur_hash_finalize(hash_value):
    hash_value = (hash_value ^ (hash_value >> 16)) & 0xFFFFFFFF
    hash_value = (hash_value * 0x85EBCA6B) & 0xFFFFFFFF
    hash_value = (hash_value ^ (hash_value >> 13)) & 0xFFFFFFFF
    hash_value = (hash_value * 0xC2B2AE35) & 0xFFFFFFFF
    hash_value = (hash_value ^ (hash_value >> 16)) & 0xFFFFFFFF
    return hash_value

def hash(data):
    if isinstance(data, str):
        data = data.encode('ascii')
    
    length = len(data)
    # Use the global SEED variable
    hash_val = SEED
    
    c1 = 0xCC9E2D51
    c2 = 0x1B873593
    
    num_chunks = length // 4
    for i in range(-num_chunks, 0):
        chunk_offset = (num_chunks + i) * 4
        
        chunk = 0
        for j in range(4):
            chunk |= data[chunk_offset + j] << (j * 8)
        
        chunk = (chunk * c1) & 0xFFFFFFFF
        chunk = ((chunk << 15) | (chunk >> 17)) & 0xFFFFFFFF
        chunk = (chunk * c2) & 0xFFFFFFFF
        hash_val ^= chunk
        hash_val = ((hash_val << 13) | (hash_val >> 19)) & 0xFFFFFFFF
        hash_val = ((hash_val * 5) - 0x19AB949C) & 0xFFFFFFFF
    
    remaining = length & 3
    if remaining > 0:
        tail = 0
        tail_start = num_chunks * 4
        
        if remaining == 3:
            tail ^= data[tail_start + 2] << 16
        if remaining >= 2:
            tail ^= data[tail_start + 1] << 8
        if remaining >= 1:
            tail ^= data[tail_start]
        
        tail = (tail * c1) & 0xFFFFFFFF
        tail = ((tail << 15) | (tail >> 17)) & 0xFFFFFFFF
        tail = (tail * c2) & 0xFFFFFFFF
        hash_val ^= tail
    
    hash_val ^= length
    return murmur_hash_finalize(hash_val)
