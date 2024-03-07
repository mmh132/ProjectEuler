from itertools import product
from math import gcd

def tot(n):
    rv = 1
    i = 2
    while n > 1:
        e = 0
        while n%i == 0:
            n//=i
            e += 1
        if e != 0:
            rv *= (i-1) * i ** (e-1)
        i += 1
    return rv

def bf(n):
    rv = 0
    for i in product(range(n), repeat = 6):
        if gcd(sum(j*j for j in list(i)), n*n) == 1:
            rv += 1
    return rv

def bfG(n):
    rv = 0
    for i in range(1, n + 1):
        rv += bf(i)//i//i//tot(i)
    return rv

# print(bfG(10))

# print([i for i in product(range(3), repeat = 3)])
L = 11
# print([(bf(i), i) for i in range(1, L + 1)])
# print([(bf(i)//i//i//tot(i), i) for i in range(1, L + 1)])


#linear sieve assuming g(p^n) = p^3g(p^n-1)

def lsieve(n):
    isc, vals, primes = [0]*(n + 1), [0]*(n + 1), []
    vals[1] = 1
    for i in range(2, n + 1):
        if not isc[i]:
            primes.append(i)
            vals[i] = i**3 + (1 if i%4 == 3 else (-1 if i%4 == 1 else 0))
        for p in primes:
            if i*p > n: break
            isc[i*p] = 1
            if i*p == 6: print(vals[i] * vals[p])
            if i % p:
                vals[i*p] = vals[i] * vals[p]
            else:
                vals[i*p] = vals[i] * p ** 3
                break
    return sum(vals) % (10**9 + 7)

print(lsieve(10**5))