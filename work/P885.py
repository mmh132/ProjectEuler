from functools import cache

MOD = 1123455689

@cache
def fac(n):
    if n < 2: return 1
    return n*fac(n-1)

def ctperms(l):
    hits = dict()
    for i in l:
        if i in hits: 
            hits[i] += 1
        else:
            hits[i] = 1
    
    n, d = 0, 1
    for i in hits:
        n += hits[i]
        d *= fac(hits[i])

    return fac(n)//d

def pv(l):
    rv = 0
    for i in range(1, len(l) + 1):
        rv += 10**(i-1) * l[-i]
    return rv

def dp(n, i, l):
    if n == 0:
        return pv(l) * ctperms(l)
    rv = 0
    for j in range(i, 10):
        rv += dp(n-1, j, l + [j])
    return rv % MOD

print(dp(18, 0, []))

