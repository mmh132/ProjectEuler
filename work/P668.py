from math import isqrt
from functools import cache as ccc
import sys
# from util.prime import lucy as lucy
sys.setrecursionlimit(10000)

def f(n):
    rt = isqrt(n)
    isp = [1]*(rt+1)
    for i in range(2, isqrt(rt) + 1):
        if not isp[i]: continue
        for k in range(i+i, rt+1, i):
            isp[k] = 0
    primes = []
    for i in range(2,rt+1):
        if isp[i]: primes.append(i)
    print(primes)
    cache = dict()
    def smooth(n, k):
        if k == 0:
            return len(bin(n)) - 2
        if (n,k) in cache: return cache[(n,k)]
        p = primes[k]
        if p > n: return n
        x = 1
        rr = 0
        while x<=n:
            rr += smooth(n//x, k-1)
            x*=p
        cache[(n,k)] = rr
        return rr

    out = len(bin(n)) - 4
    for i,p in enumerate(primes):
        if p == 2: continue
        out += smooth(n//p, i) - smooth(p, i)
        print(p)
        todel = []
        for tt in cache:
            if tt[1] - i < -1:
                todel.append(tt)
        for tt in todel:
            del cache[tt]
        del todel
    return out

print(f(10**8))

def squarefree(n):
    rt = isqrt(n)
    m = [1]*(rt+1)
    p = [1]*(rt+1)
    for i in range(2, rt+1):
        if not p[i]: continue
        m[i] = -1
        for k in range(i+i, rt+1, i):
            m[k]*=-1
            p[k] = 0
        for k in range(i*i, rt+1, i*i):
            m[k] = 0
    rv = 0
    for i in range(1, rt+1):
        rv += m[i]*(n//i//i)
    return rv

    



            
   
