from math import isqrt
cache = dict()
def totientsumslow(n):
    if n in cache: return cache[n]
    rv = n*(n+1) >> 1
    for g in range(2, isqrt(n) + 1):
        rv -= totientsumslow(n//g)
    for z in range(1, isqrt(n) + 1):
        if n//z != z:
            rv -= (n//z - n//(z+1))*totientsumslow(z)
    cache[n] = rv
    return rv

def lsieve(n):
    rv = list(range(n+1))
    for i in range(2, n+1):
        if rv[i] == i:
            rv[i] = i-1
            for k in range(i+i, n+1, i):
                rv[k] //= i
                rv[k] *= (i-1)
    return rv

def totientsumfast(n):
    y = int(n**(2/3))
    tot = lsieve(y)
    T = dict()

    for i in range(2, len(tot)):
        tot[i] += tot[i-1]

    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        if la <= y: 
            T[la] = tot[la]
        else:
            put = la*(la+1) >> 1
            for k in range(1, isqrt(la) + 1):
                put -= (tot[k] - tot[k-1])*(la//k)
                if k != 1:
                    put -= T[la//k]
            put += T[isqrt(la)]*isqrt(la)
            T[la] = put
        i = la + 1

    return T[n]

z = 10**4

print(totientsumfast(z))

print(totientsumslow(z))

print(pow(2, (10**11 + 1)*(10**11 + 1), 10**8))