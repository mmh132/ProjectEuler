def binpow(base, exp, mod):
    rv = 1
    base %= mod
    while exp:
        if exp & 1: 
            rv = rv*base % mod
        base = base*base % mod
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

