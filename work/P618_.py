from math import isqrt
from functools import cache
import sys
sys.setrecursionlimit(1000000)
MOD = 10**9
def S(n):
    p = [1]*(n+1)
    for i in range(2,isqrt(n) + 1):
        if not p[i]: continue
        for k in range(i, n+1, i):
            p[k] = 0
    primes = [i for i in range(2, n+1) if p[i]]
    @cache
    def SS(n, mp):
        if mp >= len(primes) or primes[mp] > n:
            return 0
        rv = 0
        for exp in range(n//primes[mp]+1):
            rv += SS(n-primes[mp]*exp, mp+1)*pow(primes[mp], exp, MOD)
            rv %= MOD
        return rv
    return SS(n, 0)
def fib(n):
    f1,f2,f3 = 0,0,1
    n-=1
    while n:
        f1 = f2
        f2 = f3
        f3 = f1+f2
        n-=1
        yield(f3)
print(S(8))
# wewant = 0
# for i in fib(24):
#     wewant += S(i)
#     print(i)
#     wewant %= MOD
# print(wewant)
    
    
    
    