from functools import cache

MOD = 1123455689

@cache
def fac(n):
    if n < 2: return 1
    return n*fac(n-1)

def ctperms(l, t):
    l.sort()
    if len(l) == 0: return 0
    s = 0
    if l[0] == 0 and not t:
        l.pop(0)
        s = -ctperms(l, True)
        l.append(0)
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
    return s + fac(n)//d

def dp(n, i, l):
    if n == 0:
        z = ctperms(l, False)
        #print(l, z*(z-1)//2, z)

        return (z - 1)*z//2
    rv = 0
    for j in range(i, 10):
        rv += dp(n-1, j, [j] + l)
    return rv % MOD

print(ctperms([2, 3, 0 ,2], False))

print(dp(3, 0, []))
