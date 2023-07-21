from math import isqrt

def mobius(n):
    mob = list(range(n+1))
    prime = [1]*(n+1)
    for i in range(2, n+1):
        if prime[i]:
            mob[i] *= -1
            for j in range(i+i, n+1, i):
                mob[j]*=-1
                prime[j] = 0
            for j in range(i**2, n+1, i**2):
                mob[j] = 0
    return mob

def sumdiv(n):
    rv = 0
    r = isqrt(n)
    for i in range(1, r + 1):
        rv += (n//i)*i
        rv += ((n//i+1)*(n//i))//2
    rv -= r*r*(r+1)//2
    return rv

def lsievediv(n):
    div = [1]*(n+1)
    for i in range(1, n+1):
        for k in range(i, n+1, i):
            div[k] += i
    return div

def finalsum(n):
    rv = 0

    g = mobius(isqrt(n))
    G = g.copy()

    div = lsievediv(isqrt(n))

    for i in range(1, len(g)):
        G[i] += G[i-1]
    
    for i in range(1, isqrt(n) + 1):
        rv += g[i] * sumdiv(n//(i*i))

    return rv - n*(n+1)//2

print(finalsum(10**14) % (10**9 + 7))