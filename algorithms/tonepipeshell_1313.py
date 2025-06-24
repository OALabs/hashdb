# Created by Still Hsu <still@teamt5.org>

DESCRIPTION = "TOnePipeShell hash with seed 0x521 (1313)"
TYPE = 'unsigned_int'
TEST_1 = 3354381195


def hash(data):
    out_hash = 0
    for c in data:
        out_hash = (c + 1313 * out_hash) & 0xffffffff
    return out_hash
