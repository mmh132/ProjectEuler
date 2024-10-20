from math import comb, factorial
from functools import cache
MOD = 10**9 + 7
N = 50
N *= 3

def fac(n):
    rv = 1
    for i in range(2, n+1):
        rv *= i
        rv %= MOD
    return rv

@cache
def comb(n, k):
    if n == k or k == 0 or n == 0: return 1
    if k > n or k < 0: return 0
    return (comb(n-1, k) + comb(n-1, k-1)) % MOD

@cache
def pow2(n, k, MOD):
    if k == -1: return pow(n, k, MOD)
    rv = 1
    while k:
        if k & 1: rv = (rv * n) % MOD
        n = (n*n) % MOD
        k //= 2
    return rv

@cache
def f(q1,q2,q3,q4):
    if q1<0 or q2<0 or q3<0 or q4<0: return 0
    if q1 == q2 == q3 == q4 == 0: return 1
    rv = 0
    for f1 in range(min(4, q1 + 1)):
        for f2 in range(min(4-f1, q2 + 1)):
            for f3 in range(min(4-f1-f2, q3 + 1)):
                f4 = 3-f1-f2-f3
                if f4 > q4: continue
                ta = comb(q1, f1) * comb(q2, f2) * comb(q3, f3) * comb(q4, f4) * f(q1 - f1 + f2, q2 - f2 + f3, q3 - f3 + f4, q4-f4) % MOD
                ta = ta * pow2(4, f4, MOD) * pow2(3, f3, MOD) * pow2(2, f2, MOD) % MOD
                rv = (rv + ta) % MOD 
    return rv

print(f(0,0,0,N) * pow(fac(N//3 * 4), -1, MOD) % MOD)