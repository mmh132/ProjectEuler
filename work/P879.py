from math import gcd
from functools import cache

SIZE = 4

def topt(n):
    assert 0 <= n < SIZE*SIZE
    return (n//SIZE, n%SIZE)

def ton(pt):
    assert 0 <= pt[0] < SIZE and 0 <= pt[1] < SIZE
    return pt[0]*SIZE + pt[1]

@cache
def dp(mask, last, lastslope):
    lp = topt(last)
    rv = 1
    for dir in range(SIZE*SIZE):
        if mask & (1 << dir): continue
        fp = topt(dir) 
        d = gcd((fp[0] - lp[0]), (fp[1] - lp[1]))
        slope = ((fp[0] - lp[0])//d, (fp[1] - lp[1])//d)
        if slope == lastslope: continue
        nm = 0
        for i in range(d + 1):
            nm += 1 << ton((lp[0] + slope[0]*i, lp[1] + slope[1]*i))
        rv += dp(mask | nm, dir, slope)
    return rv

out = 0
for i in range(SIZE*SIZE):
    out += dp(1 << i, i, (0,0))
print(out - SIZE*SIZE)