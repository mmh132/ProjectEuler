from math import lcm, isqrt
def f(n):
    sets = {1: 1}
    for i in range(1, n+1):
        ns = sets.copy()
        for key in sets:
            nv = lcm(key, i)
            if nv not in ns: 
                ns[nv] = 0
            ns[nv] += sets[key]
        sets = ns.copy()
        print(i, len(sets))
    rv = 0
    for key in sets:
        rv += sets[key]*key 
        rv %= (10**9 + 7)
    return rv

print(f(20))

def ff(n):
    primes = [1]*(n+1)
    for i in range(2, n+1):
        if primes[i]:
            for k in range(i, n+1, i):
                primes[k] = 0
    lprimes = [i for i in range(2, n+1) if primes[i]]
    larges = [i for i in lprimes if i > isqrt(n)]
    largect = [0]*(len(larges))
    sets = {1: 2}
    for j in range(2, n+1):
        i = j
        for p, idx in enumerate(larges):
            if j%p == 0:
                largect[idx] += 1
                print(j, p, idx)
                i//=p
        ns = sets.copy()
        for key in sets:
            nv = lcm(key, i)
            if nv not in ns: 
                ns[nv] = 0
            ns[nv] += sets[key]
        sets = ns.copy()
    print(largect)

print(ff(20))
    