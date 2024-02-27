from math import isqrt
import time

N = 10**6

def squarefree(n):
    rt = isqrt(n)
    primes, cmp, mu = [],[0]*(rt+1),[0]*(rt+1)
    mu[1] = 1
    for i in range(2, rt+1):
        if not cmp[i]:
            primes.append(i)
            mu[i] = -1
        for j in primes:
            idx = i*j
            if idx > rt: break
            cmp[idx] = True
            if i%j == 0:
                mu[idx] = 0
                break
            else:
                mu[idx] = mu[i]*-1
    
    rv = 0
    for i in range(1, rt + 1):
        rv += mu[i]*(n//i//i)
    return rv

def sieve(n):
    S = 10**5
    primes, oprimes = [], []
    rt = isqrt(n)
    
    isp = [1]*(rt + 1)
    for i in range(2, rt + 1):
        if isp[i]:
            primes.append(i)
            for k in range(i*i, rt, i):
                isp[k] = 0
    
    for k in range(n//S):
        block = [1] * S
        start = k*S
        for p in primes:
            i = (start + p - 1) // p
            for j in range(max(i, p)*p - start, S, p):
                block[j] = 0
        if k == 0:
            block[0] = 0
            block[1] = 0

        for i in range(S):
            if start + i > n: break
            if block[i]:
                oprimes.append(start + i)
    
    return primes + oprimes

def iroot(n, i):
    l, h, m = 1, n, 0
    while h - l > 1:
        m = (l+h) // 2
        h, l = (m, l) if pow(m, i) > n else (h, m)
    if pow(l+1, i) <= n:
        l += 1
    return l

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

def lucy(n):
    S = dict()
    for i in FIinc(n):
        S[i] = i-1
    for p in range(2, isqrt(n) + 1):
        if S[p] == S[p-1]: continue
        for v in FIdec(n):
            if v < p*p: break
            S[v] -= (S[v//p] - S[p-1])
    return S

def countSignature(sig, x):
    def rec(i,j,x,rem):
        if i == len(sig) - 1:
            w = iroot(x,sig[i])
            return max(0, lcy[w] - j)
        t = 0
        for k in range(j,len(primes)):
            if primes[k]**rem > x: break
            t += rec(i+1, k+1, x//primes[k]**sig[i], rem-sig[i])
        return t
    return rec(0, 0, x, sum(sig))

lcy = lucy(N)
primes = sieve(isqrt(N) + 100)

def rec2(cs):
    print(cs)
    rv = countSignature(cs, N)
    if rv == 0 or cs[-1] == 0: return 0
    next = 1
    x = rec2(cs.copy() + [next])
    while x > 0 and next <= cs[-1]: 
        rv += x
        next += 1
        x = rec2(cs.copy() + [next])
    return rv

i = 2
cs = rec2([i])
out = squarefree(N) + cs
while cs > 0:
    i += 1
    cs = rec2([i])
    out += cs
print(out)


