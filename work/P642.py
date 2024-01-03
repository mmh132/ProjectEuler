from math import isqrt
import sys
sys.setrecursionlimit(100000)

def FIinc(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield la
        i = la + 1
        
def FIdec(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield n//la
        i = la + 1

def f(n):
    lim = int(n**(2/5))
    
    vals = dict()
    primes = []
    for i in FIinc(n):
        vals[i] = i*(i+1)//2 - 1
    for p in range(2, isqrt(n) + 1):
        if vals[p] == vals[p-1]: continue
        primes.append(p)
        for v in FIdec(n):
            if v < p*p: break
            vals[v] -= p*(vals[v//p] - vals[p-1])

    cache = dict()
    def smooth(n, i):
        if (n, i) in cache: 
            return cache[(n, i)]
        if n == 0:
            return 0
        if i == -1:
            return 1
        rv = smooth(n, i-1) + smooth(n//primes[i], i)
        if n < lim:
            cache[(n, i)] = rv
        return rv
    
    rv = 0
    for i in range(len(primes)):
        p_i = primes[i]
        rv += p_i*smooth(n//p_i, i)
        #print(smooth(n//p_i, i), p_i, n//p_i)
    for i in range(1, isqrt(n)):
        #print(vals[n//i] - vals[n//(i+1)])
        rv += (vals[n//i] - vals[n//(i+1)])*i
    return rv

print(f(201820182018))