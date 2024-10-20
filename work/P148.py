from math import isqrt
from itertools import product

def factor(n):
    rv = []
    i = 2
    while n != 1:
        while n%i == 0: rv.append(i); n//=i
        i+=1
    return rv

def pff(n):
    rv = dict()
    for i in range(2, n + 1):
        for j in factor(i):
            if j in rv: rv[j] += 1
            else: rv[j] = 1
    return rv

def enumdivs(n):
    dd = pff(n)
    keys = [i for i in dd]
    rv = []
    def dp(i, n):
        if i >= len(keys): rv.append(n); return 
        for e in range(dd[keys[i]] + 1):
            dp(i+1, n*keys[i]**e)
    dp(0, 1)
    return rv

print(enumdivs(13))

def isprime(n):
    for i in range(2, isqrt(n) + 1):
        if not n%i: return False
    return True


fac = (10, 5, 2, 1, 1, 1)
primes = [2, 3, 5, 7, 11, 13]

def ton(mask):
    rv = 1
    for i in range(6): rv *= primes[i]*mask[i]
    return rv

def tomask(n):
    rv = [0,0,0,0,0,0]
    for i in range(6):
        while n % primes[i]:
            n //= primes[i]
            rv[i] += 1
    if n == 1: return rv
    return False

def masktoidx(m):
    

def enumdivs(mask):
    for z in product(*[range(mask[i] + 1) for i in range(6)]):
        yield z

pairs = []

for i in primes:
    pairs.append((i, tomask(i-1)))

for i in enumdivs(fac):
    v = ton(i)
    if isprime(v + 1):
        pairs.append((v + 1, i))


