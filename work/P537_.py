from math import log
from functools import cache
import sys
sys.setrecursionlimit(100000)
MOD = 1004535809
def t(n):
    n += 1
    p = [1]*int(n*log(n) + n*log(log(n)))
    for i in range(2, len(p)):
        if p[i]:
            for k in range(i+i, len(p), i):
                p[k] = 0
    p[0] = p[1] = 0
    n -=1 
    pivals = [0]*(n+1)
    cv = 0
    i = 1
    while cv <= n:
        pivals[cv] += 1
        cv += 1 if p[i] else 0
        i += 1
    pivals[0] = 1
    @cache
    def dp(n, k):
        if k == 0: return 1 if n == 0 else 0
        rv = 0
        for idx, val in enumerate(pivals):
            if n-idx < 0: break
            rv += dp(n-idx,k-1)*val
            rv %= MOD
        return rv
    return dp(n, n)

print(t(10))