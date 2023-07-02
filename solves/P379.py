from math import gcd
import time
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

def isqrt(x):
    if x == 1: return 1
    a = x >> 1
    b = x
    while a < b:
        c = (a + x//a) >> 1
        a,b = c,a
    return b


def speedyf(n):
    msieve = mob(isqrt(n))
    s = 0
    for k in range(1, isqrt(n) + 1):
        s += msieve[k]*H(n//k//k)
    return s

memo = dict()
def H(n):
    if n in memo: return memo[n]
    s = 0
    for i in range(1, isqrt(n) + 1):
        s += n//i
    s -= (isqrt(n)**2)//2
    return s

def fasterg(n):
    s = 0
    for d in range(1, isqrt(n) + 1):
        s += speedyf(n//d)
    for z in range(1, isqrt(n) + 1):
        if n//z != z:
            s += (n//z - n//(z+1))*speedyf(z)
    return s


print(fasterg(10**12) + 10**12 // 4)
# print(fastergnotrick(10**5))
# print(sqrttricknoalt(10**5))