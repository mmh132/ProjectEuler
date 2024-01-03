from math import gcd
from functools import cache

@cache
def t(n):
    if n == -1: return 0
    if n == 0: return 1
    return 10*t(n-1) + t(n-2)

print(t(1), t(2), t(3), t(4))

def s(l):
    rv = 0
    for a in range(1, l+1):
        for b in range(1, l+1):
            for c in range(1, l+1):
                rv += gcd(t(c**a), t(c**b))
    return rv

print(s(3))