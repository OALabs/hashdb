DESCRIPTION = "Castle Loader API hash"
TYPE = "unsigned_int"
TEST_1 = 420894349


def hash(data):
    hash_val = 0xAAAAAAAA
    is_odd = 0
    for _, curr_char in enumerate(data):
        tmp = 0
        if (is_odd & 1) != 0:
            val1 = (hash_val << 11) & 0xFFFFFFFF
            val2 = (curr_char ^ (hash_val >> 5)) & 0xFFFFFFFF
            tmp = (~(val1 + val2)) & 0xFFFFFFFF
        else:
            val1 = (hash_val << 7) & 0xFFFFFFFF
            val2 = (curr_char * (hash_val >> 3)) & 0xFFFFFFFF
            tmp = (val1 ^ val2) & 0xFFFFFFFF
        hash_val = (hash_val ^ tmp) & 0xFFFFFFFF
        is_odd += 1
    return hash_val
