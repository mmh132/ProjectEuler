import sys
from math import isqrt
sys.setrecursionlimit(10000000)
N = 10**14

def sieve(n):
    p = [1]*(n+1)
    for i in range(2, n+1):
        if not p[i]: continue
        for k in range(i+i, n+1, i):
            p[k] = 0
    rv = []
    for i in range(2, n+1):
        if p[i]: rv.append(i)
    return rv

primes = sieve(isqrt(N))

mem = dict()
def h(p, e):
    if e == 0:
        return 1
    if e == 1:
        return 0
    if (p,e) in mem: return mem[(p,e)]
    x = pow(p, e-1 if e&1 else e)
    for i in range(e):
        x -= h(p, i)
    mem[(p,e)] = x
    return x

def solve():
    rv = [0]
    def dfs(n, hn, p):
        #print(n, hn, p)
        if p >= len(primes) or n > N:
            rv[0] += hn*(N//n)
            return
        e = 2
        while n*primes[p]**e <= N:
            dfs(n*pow(primes[p],e), hn*h(primes[p], e), p+1)
            e+=1
        if e != 2:
            dfs(n, hn, p+1)
        else:
            rv[0] += hn*(N//n)
        return
    dfs(1,1,0)
    return rv[0] % (10**9 + 7)

print(solve())
