from math import isqrt

def generalconvolve(f,g,F,G,n, mod = 0):
    rv = 0
    for i in range(1, isqrt(n) + 1):
        rv += f(i)*G(i)
        rv += g(i)*F(i)
        if mod: rv %= mod
    rv -= F(isqrt(n))*G(isqrt(n))
    if mod: rv += mod; rv %= mod
    return rv

def backtrack(f,g,h,G,H,n, mod = 0):
    
