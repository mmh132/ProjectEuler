from math import isqrt
from functools import cache







def FIinc(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield la
        i = la + 1
        
def FIdec(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield n//la
        i = la + 1

N, M, MOD = 10**6, 510510, 10**9
Y = max(int(N**(2/3)), M)

tot, cmp, primes = [0]*(Y+1), [0]*(Y+1), []
tot[1] = 1
for i in range(2, Y+1):
    if not cmp[i]:
        primes.append(i)
        tot[i] = i-1
    for j in primes:
        idx = i*j
        if idx > Y: break
        cmp[idx] = 1
        if i % j == 0:
            tot[idx] = tot[i] * j
        else:
            tot[idx] = tot[i] * (j - 1)

for i in range(2, Y+1):
    tot[i] += tot[i-1]

T = {}
for i in FIinc(N):
    if i <= Y:
        T[i] = tot[i]
        continue
    put = i*(i+1)//2
    for j in range(1, isqrt(i) + 1):
        put -= (tot[j])*(i//j)
        put -= T[i//j] if j != 1 else 0
    put += T[isqrt(i)]*isqrt(i)
    T[i] = put % MOD

for i in range(Y, 1, -1):
    tot[i] -= tot[i-1]

def s_bf(p, n):
    rv = 0
    for i in range(1, n+1):
        rv += tot[i*p]
    return rv

def s_test(p, n):
    if n < 1: return 0
    if n == 1: return 1
    rv = 0
    for i in range(1, n+1):
        rv += tot[i]
    rv *= tot[p]
    rv += s_test(p, n//p)
    return rv


def s_bf_2(p,q, n):
    rv = 0
    for i in range(1, n+1):
        rv += tot[i*p*q]
    return rv

def s_test_2(p,q,n):
    if n < 1: return 0
    if n == 1: return 1
    rv = 0
    for i in range(1, n+1):
        rv += tot[i]
    rv *= tot[p*q]
    rv += tot[q]*s_test(p,n//p)
    rv += tot[p]*s_test(q,n//q)
    rv += s_test_2(p, q, n//p//q)
    return rv

print(s_bf_2(5,7, 100), s_test_2(5,7, 100))

    

@cache
def d(n):
    rv = set()
    for i in range(1, isqrt(n) + 1):
        if not n%i:
            rv.add(i)
            rv.add(n//i)
    return tuple(rv)

def s(x, n):
    if n < 1: return 0
    if n == 1: return tot[x]
    if x == 1: return T[n]
    rv = 0
    for i in d(x):
        for j in d(n//i):
            rv += s(i, n//i)*tot[j]
        rv %= MOD
    return rv

print(s(5*7, 100))
print(s(510510, 10**6))

































