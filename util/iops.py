from math import comb

def sumpow(n, exp, mod = 0):
    rv = 0
    if n > exp:
        for i in range(1, exp+1):
            for j in range(i):
                rv += pow(-1, j)*pow(i-j, exp)*comb(n+exp-i+1, n-i)*comb(exp+1, j)
                if mod: rv %= mod
    else:
        for i in range(1,n+1):
            rv += pow(i, exp)
            if mod: rv %= mod
    return rv

#convention is r^0 or r*0 as first term
def geometricseries(a1, r, n, mod = 0):
    if mod:
        return (a1*(pow(r, n, mod) - 1)*pow(r-1, -1, mod)) % mod
    else:
        (a1*(pow(r, n) - 1)//(r-1))

def arithmeticseries(a1, r, n, mod = 0):
    if mod:
        return (n*a1 + r*n*(n-1)//2) % mod
    else:
        return (n*a1 + r*n*(n-1)//2)

def isqrt(x):
    if x == 1: return 1
    a = x >> 1
    b = x
    while a < b:
        c = (a + x//a) >> 1
        a,b = c,a
    return b

def binpow(b, e, mod = 0):
    rv = 0
    while e:
        if b & 1:
            rv = rv*b
            if mod: rv %= mod
        b = b*b
        if mod: b %= mod
    return rv

# returns a,b,gcd(x,y) where ax+by = gcd(x,y)
def extEuclidean(x,y):
    flip = False
    if y > x: x,y = y,x; flip = True
    s0,s1 = 1,0
    t0,t1 = 0,1
    while y:
        q = x//y
        x,y = y,x%y
        s0,s1 = s1, s0 - q*s1
        t0,t1 = t1, t0 - q*t1
    if flip:
        return (t1, s1, x)
    return (s1, t1, x)

def modinv(x, m):
    x %= m
    return extEuclidean(x,m)[0] % m