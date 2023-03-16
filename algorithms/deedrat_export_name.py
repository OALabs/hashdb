# Created by Still Hsu <still@teamt5.org>

DESCRIPTION = "Hashing algorithm for library export name used by DeedRAT."
TYPE = 'unsigned_int'
TEST_1 = 1493252751


def hash(data):
    i = 0
    ecx = 0
    eax = 0
    edi = 0
    esi = 0
    for c in data:
        i = i+1
        edi = c
        ecx = esi
        eax = esi
        if i & 1 != 0:
            ecx = (ecx << 0x5) & 0xffffffff
            eax = (eax >> 0x1) & 0xffffffff
            ecx = ecx ^ eax
            ecx = ecx ^ edi
        else:
            ecx = (ecx << 0x9) & 0xffffffff
            eax = (eax >> 0x3) & 0xffffffff
            ecx = ecx ^ eax
            ecx = ecx ^ edi
            ecx = ~(ecx) & 0xffffffff
        esi = esi ^ ecx
    return esi & 0x7fffffff
