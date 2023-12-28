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

def sum_nk(n, k, mod):
    pts = [(1,1)]
    while len(pts) <= k+2:
        x = pts[-1]
        pts.append((x[0]+1, (x[1]+pow(x[0]+1, k, mod))%mod))
    np = [pts.pop(0)]
    while pts:
        x = pts.pop(0)
        np.append((x[0], (np[-1][1] + x[1]) % mod))
    pts = np.copy()
    rv = 0
    t = 1
    for i in pts:
        t*=(n-i[0])
        t %= mod
    for i in pts:
        b = 1
        for j in pts:
            if i==j: continue
            b*=(i[0]-j[0])
            b%=mod
        rv += pow(b, -1, mod)*pow(n-i[0], -1, mod)*t*i[1]
        rv %= mod
    return rv

tp = 0
for i in range(2*10**9, 2*10**9 + 2001):
    if MillerRabin64(i):
        tp += sum_nk(10**12, 10_000, i)
        print(i)
print(tp)