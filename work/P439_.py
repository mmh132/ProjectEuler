from functools import cache
from math import isqrt

def FIinc(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield la
        i = la + 1

MOD = 10**9

def nc2(n): 
    return n*(n+1)//2 % MOD 

@cache
def ss(n):
    rv, rt = 0, isqrt(n)
    for i in range(1, rt + 1):
        rv = (rv + i*(n//i) + nc2(n//i)) % MOD
    rv = (rv - rt*nc2(rt)) % MOD
    return (rv*rv) % MOD

@cache
def S(n):
    rv, la = ss(n), 1
    for i in FIinc(n):
        if i == 1: continue
        rv = (rv - (nc2(i)-nc2(la))*S(n//i)) % MOD
        la = i
    return rv

print(S(10**11))
