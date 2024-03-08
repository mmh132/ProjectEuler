import sys
from math import isqrt
from functools import cache

N = 10**14
rt = isqrt(N)

@cache
def d(n):
    rv = 0
    for i in range(1, isqrt(n) + 1):
        rv += 2*(n//i)
    return rv - isqrt(n)*isqrt(n)

p = [0,0] + [1]*(rt - 1)
for i in range(2, isqrt(rt) + 1):
    p[i*i::i] = [0]*((rt - i*i)//i + 1)

primes = [i for i in range(2, rt + 1) if p[i]]

@cache
def h(p, e):
    if e < 2: return 0 if e == 1 else 1
    x = pow(2, e)
    for i in range(e):
        x -= h(p, i)*(e-i+1)
    return x

def powerfulnumbersext(N):
    stk = [(1,1,0)]
    while stk:
        nn, hn, i = stk.pop(0)
        if i >= len(primes) or primes[i]*primes[i] > N//nn:
            yield (nn, hn)
            continue
        p = primes[i]
        stk.append((nn, hn, i+1))
        e = 2
        while p**e <= N//nn:
            stk.append((nn*p**e, hn*h(p, e), i+1))
            e += 1

rv = 0
for n, hn in powerfulnumbersext(N):
    rv += d(N//n)*hn
print(rv)

                                                            