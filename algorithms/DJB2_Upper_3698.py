DESCRIPTION = "Custom hash algorithm using initial value 3698 with multiplier 33"
TYPE = 'unsigned_int'
# Hash of 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEST_1 = 3023272509

def hash(data):
    hash_value = 3698
    for byte in data:
        upper_char = byte if byte < 97 or byte > 122 else byte - 32
        hash_value = (hash_value * 33 + upper_char) & 0xFFFFFFFF
    return hash_value
