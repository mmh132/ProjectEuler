from math import gcd, isqrt
def lsieve(n):
    primes = [1]*(n+1)
    mobius = list(range(n+1))
    for i in range(2, n+1):
        if primes[i]:
            mobius[i] *= -1
            for k in range(i+i, n+1, i):
                mobius[k] *= -1
                primes[k] = 0
            for k in range(i**2, n+1, i**2):
                mobius[k] = 0
    return mobius

def N(x):
    return x*(x+1) >> 1

def N2(x): 
    return x*(x+1)*(2*x+1)//6

def fastinv(n):
    g = lsieve(isqrt(n))
    G = dict()
    G[1] = 1

    for v in range(2, isqrt(n)):
        x = 1
        for i in range(1, isqrt(v) + 1):
            x -= g[i]*N(v//i)
            if i != 1:
                x -= i*G[v//i]
        x += G[isqrt(v)]*N(isqrt(v))
        G[v] = x
    
    for z in range(isqrt(n), 0, -1):
        v = n//z
        x = 1
        for i in range(1, isqrt(v) + 1):
            x -= g[i]*N(v//i)
            if i != 1:
                x -= i*G[v//i]
        x += G[isqrt(v)]*N(isqrt(v))
        G[v] = x

    return G

mem = {0:0}
def tsum(n):
    print(n)
    if n in mem: return mem[n]
    
    rv = 0
    G = fastinv(n)
    g = lsieve(isqrt(n))

    for i in range(1, isqrt(n) + 1):
        rv += g[i]*N2(n//i)
        rv += i*i*G[n//i]
    rv -= G[isqrt(n)]*N2(isqrt(n))
    mem[n] = rv
    return rv 

def finalsum(n):
    rv = n
    for i in range(1, isqrt(n) + 1):
        rv += (tsum(i)-tsum(i-1))*(n//i)
        rv += tsum(n//i)
    rv -= (isqrt(n))*(tsum(isqrt(n)))
    return rv/2

print(tsum(33))
print(finalsum(100))
print(sum(lsieve(10000)))
print(fastinv(10000)[10000])
