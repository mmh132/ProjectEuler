from math import gcd

def isqrt(x):
    if x == 1: return 1
    a = x >> 1
    b = x
    while a < b:
        c = (a + x//a) >> 1
        a,b = c,a
    return b

def mob(n):
    primes = [1]*(n+1)
    mobius = [1]*(n+1)
    for i in range(2, n+1):
        if primes[i]:
            mobius[i] *= -1
            for k in range(i+i, n+1, i):
                mobius[k] *= -1
                primes[k] = 0
            for k in range(i**2, n+1, i**2):
                mobius[k] = 0
    return mobius

mset = dict()
def D(n):
    if n in mset: return mset[n]
    s = 0
    for i in range(1, isqrt(n) + 1):
        s += n//i
    s *= 2
    s -= isqrt(n)*isqrt(n)
    mset[n] = s
    return s

mset2 = dict()
def G(n):
    if n in mset2: return mset2[n]
    msieve = mob(isqrt(n))
    s = 0
    for i in range(1, isqrt(n) + 1):
        s += msieve[i] * D(n//(i*i))
    mset2[n] = s
    return s

def F(n):
    s = 0
    for k in range(1, isqrt(n) + 1):
        s += k*G(n//(k*k))
    return s

print(F(10**15))