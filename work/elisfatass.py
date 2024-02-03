import math
from functools import cache

def e114(n = 50):
    @cache
    def dp(n):
        if n < -1: return 0
        rv = 1
        for g in range(n):
            for r in range(3, n+1):
                rv += dp(n-g-r-1)
        return rv
    return dp(n)

def e115(ex = 1000000, m = 50):
    @cache
    def dp(n, m):
        if n < -1: return 0
        rv = 1
        for g in range(n):
            for r in range(m, n+1):
                rv += dp(n-g-r-1, m)
        return rv
    i = m
    while dp(i, m) < ex:
        i += 1
    return i

def e116(n = 50, sz = [2,3,4]):
    @cache
    def dp(n, s):
        if -1 < n < s:
            return 1
        if n < 0:
            return 0
        rv = 1
        for i in range(s, n+1):
            rv += dp(n-i, s)
        return rv
    return sum([dp(n, x) for x in sz]) - 3

def e117(n = 50, sz = [2,3,4]):
    @cache
    def dp(n):
        if -1 < n < min(sz):
            return 1
        if n < 0:
            return 0
        rv = 1
        for i in range(n+1):
            for s in sz:
                rv += dp(n-i-s)
        return rv
    return dp(n) 

    
def e250():
    vals = [pow(i, i, 250) for i in range(1, 250251)]
    c = [1] + [0]*249
    mod = 10**16
    for i in vals:
        nc = c.copy()
        for j in range(len(nc)):
            nc[(j+i) % 250] += c[j]
            nc[(j+i) % 250] %= mod 
        c = nc.copy()
    return c[0] - 1

def e164(N = 20):
    @cache
    def dp(n, a, b):
        if n == 0: return 1
        rv = 0
        for d in range(0, 10-a-b):
            rv += dp(n-1, b, d)
        return rv
    return dp(N, 0, 0) - dp(N-1, 0, 0)

def e169(n=10**25):
    @cache
    def dp(n):
        if n < 2: return 1
        return dp(n >> 1) + (dp(n >> 1 - 1) if not n&1 else 0)
    return dp(n)
        


def e301(n=2**30):
    rv = 0
    for i in range(1, n+1):
        if (i^2*i^3*i) == 0:
            rv += 1
    return rv

print(e301())