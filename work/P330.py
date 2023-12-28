from math import comb, factorial as fac
from functools import cache

mod = 11

@cache
def a(n):
    if n < 0: return 1
    rv = 0
    for i in range(1, n+1):
        rv += comb(n, i)*a(n-i)
    return rv + fac(n)

print(a(10))

@cache
def b(n):
    if n < 0: return 0
    rv = 0
    op = 0
    for i in range(1, n+1):
        rv += comb(n, i)*b(n-i)
        op += fac(n)/fac(i)
    return rv - op - fac(n)

print(b(10))
    
print([a(i) % mod for i in range(100)])

print([int(b(i)) % mod for i in range(100)])