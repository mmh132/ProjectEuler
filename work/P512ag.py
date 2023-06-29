def td(n):
    pfs = set()
    d = 2
    while d*d <= n:
        while n%d == 0: n//=d; pfs.add(d)
        d+=1
    if n != 1: pfs.add(n)
    return pfs

def g(n):

    rv = 0
    for i in range(1, n+1):
        if i%100000 == 0: print(i/n)
        if not i&1: continue
        t,b = 1,1
        for x in td(i):
            t *= (x-1)
            b *= x
        t %= (i+1)
        inv = pow(b, -1, i+1)
        rv += ((t*inv*-1)%(i+1) + i + 1) % (i+1)
    return rv

print(g(5*10**8))
        