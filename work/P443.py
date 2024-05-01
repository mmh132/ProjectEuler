from math import gcd
from functools import cache
from time import time

# def factor(n):
#     rv = []
#     for i in range(2, n + 1):
#         while n % i == 0:
#             n//=i
#             rv.append(i)
#     return rv

mem = {4: 13}
def g(n):
    if n in mem: return mem[n]
    mem[n] = g(n - 1) + gcd(n, g(n - 1))
    return mem[n]
# L = 10000

# for i in range(4, L):
#     print(i, "->", g(i))

# for i in range(5, L):
#     print(i, "->", g(i) - g(i-1))

# for i in range(4, L):
#     print(i, "->", g(i), g(i)/i)

# for i in range(4, L):
#     if g(i)/i == 3:
#         print(i, factor(i), 2*i - 1)

def binpow(base, exp, mod):
    rv = 1
    while exp:
        if exp & 1: rv = rv * base % mod
        base = base * base % mod
        exp >>= 1
    return rv

def checkcomposite(base, exp, mod, twopow):
    x = binpow(base,exp,mod)
    if x == 1 or x == mod-1:
        return False
    for r in range(1,twopow):
        x = (x*x) % mod
        if x == mod-1:
            return False
    return True

def MillerRabin64(n):
    if n<2: return False
    twopow = 0
    d = n-1
    while d&1 == 0:
        d>>=1
        twopow+=1
    for a in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n == a: return True
        if checkcomposite(a,d,n,twopow): return False
    return True

t = time()
N = 10**9
n, gg = 4, g(4)
while n < N:
    if 3*n == gg and MillerRabin64(2 * n - 1) and 2 * n - 1 < N:
            mem = dict()
            mem[2 * n - 1] = 3 * (2 * n - 1)
            n, gg = 2 * n - 1, g(2 * n - 1)
    else:
        n, gg = n + 1, g(n + 1)
        
print(n, g(n), time() - t)