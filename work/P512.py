def factorsieve(n):
    blank = []
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == []:
            rv[i].append(i)
            for k in range(i+i,len(rv),i):
                rv[k].append(i)
    return rv
def g(n):
    facs = factorsieve(n)
    rv = 0
    for i in range(1, n+1):
        if not i&1: continue
        t,b = 1,1
        for x in facs[i]:
            t *= (x-1)
            b *= x
        t %= (i+1)
        inv = pow(b, -1, i+1)
        rv += ((t*inv*-1)%(i+1) + i + 1) % (i+1)
    return rv

print(g(5*10**8))
        
