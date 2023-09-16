from math import isqrt

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

def generalconvolve(f,g,F,G,n, mod = 0):
    rv = 0
    for i in range(1, isqrt(n) + 1):
        rv += f(i)*G(i)
        rv += g(i)*F(i)
        if mod: rv %= mod
    rv -= F(isqrt(n))*G(isqrt(n))
    if mod: rv += mod; rv %= mod
    return rv

stk = [(1,1,0)]
def powerfulnumberext(n, h):
    primes = []
    sieve = [1]*(isqrt(n)+1)
    for i in range(2, isqrt(isqrt(n)) + 1):
        if not sieve[i]:
            continue
        for k in range(i+i, isqrt(n)+1, i):
            sieve[k] = 0
    for i in range(2, len(sieve)):
        if sieve[i] == 1:
            primes.append(i)
    while stk:
        c = stk.pop(0)
        nn, hn, i= c[0], c[1], c[2]
        if i == len(primes): yield (nn, hn); continue
        p, e = primes[i], 0
        while nn*p**e < n:
            stk.append((nn*p**e, hn*h(p,e), i+1))
            e += 1

        
        