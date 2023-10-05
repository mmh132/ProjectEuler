from math import isqrt
from functools import cache as ccc
import sys
sys.setrecursionlimit(100000)
MOD = 1004535809
N,k = 10,10
n = 2**18
ps = [1]*(n+1)
ps[0] = 0
ps[1] = 0
for i in range(2, isqrt(n)+1):
    if ps[i] == 0:
        continue
    for k in range(i+i, n+1, i):
        ps[k] = 0
pi = [0,0]
while pi[-1] <= N:
    pi.append(pi[-1] + ps[len(pi)])
pi.pop(-1)
pivals = [0]*(N+1)
pivals[0] -= 1
for i in pi:
    pivals[i] += 1
print(len(pi))
print(pivals)
cache = dict()
N,k = 3,3
def dp(p, s):
    #print(p, s)
    if (p,s) in cache: return cache[(p,s)]
    if p == 0 or s == 0:
        if s <= N:
            return 1
        return 0
    rv = 0
    for i in range(min(N, s)):
        rv += pivals[i]*dp(p-1, s-i) % MOD
    cache[(p,s)] = rv % MOD
    return rv % MOD
print(dp(N, k))
print(k)