from math import isqrt
from itertools import product
from copy import deepcopy as dc

def ds(t1, t2):
    return tuple([t1[i] + t2[i] for i in range(6)])

def isp(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def ton(mask):
    rv = 1
    for i in range(6):
        rv *= primes[i]**mask[i]
    return rv

def tomask(n):
    print(n)
    rv = [0,0,0,0,0,0]
    for i in range(6):
        while n%primes[i] == 0:
            n//=primes[i]
            rv[i] += 1
    if n == 1:
        return tuple(rv)
    return False

def enumdivs(mask):
    for i in product(*[range(mask[i] + 1) for i in range(6)]):
        yield i

mask = (10, 5, 2, 1, 1, 1)
primes = [2,3,5,7,11,13]

pp = [[] for _ in range(1584)]
pp[0].append(1)
keys = dict()
vals = dict()

#primes
j = 0
for i in enumdivs(mask):
    keys[i] = j
    vals[j] = i
    j += 1
    v = ton(i)
    if isp(v + 1):
        pp[j - 1].append(v + 1)

build = [[] for _ in range(1584)]
build[0].append(1)
nxt = [[] for _ in range(1584)]

for i in range(1584):
    print(i)
    for j in range(1584):
        nk = ds(vals[i], vals[j]) 
        if nk in keys:
            for p in pp[j]:
                for m in build[i]:
                    nxt[keys[nk]].append(p*m)
    build = dc(nxt)

actuals = []
for i in range(1584):
    for poss in build[i]:
        x = poss
        for idx, j in vals[i]:
            if mask[idx] > j:
                if x%primes[idx] != 0:
                    break
                x *= primes[idx]**(j - mask[idx])
        actuals.append(x)

print(len(actuals))

print(sorted(actuals[150_000]))







