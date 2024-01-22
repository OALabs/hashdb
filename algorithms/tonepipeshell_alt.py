# Created by Still Hsu <still@teamt5.org>

DESCRIPTION = "TOnePipeShell hash with seed 0x4E44CB31 (1313131313)"
TYPE = 'unsigned_int'
TEST_1 = 3702427595

def hash(data):
    out_hash = 0
    for c in data:
        out_hash = (c + 0x4E44CB31 * out_hash) & 0xffffffff
    return out_hash
