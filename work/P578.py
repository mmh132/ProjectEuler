from math import isqrt, log2
import time

def iroot(n, k): 
    rv = int(n**(1/k))
    while rv ** k < n:
        rv += 1
    while rv ** k > n:
        rv -= 1
    return rv

def seg_sieve(n):
    n = int(n)
    S = 10**5

    primes = []
    nsqrt = isqrt(n)
    is_prime = [1] * (nsqrt+2)
    for i in range(2,nsqrt+1):
        if is_prime[i]:
            primes += [i]
            for j in range(i*i,nsqrt+1,i):
                is_prime[j] = 0

    result = []
    block = [0] * S
    for k in range(n//S+1):
        block[:] = [1]*S
        start = k * S
        for p in primes:
            start_idx = (start + p - 1) // p
            j = max(start_idx, p) * p - start
            while j < S:
                block[j] = 0
                j += p
        
        if k == 0:
            block[0] = block[1] = 0
        for i in range(S):
            if start + i > n:
                break
            if block[i]:
                result += [start+i]

    return result

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

S = dict()
def lucy(n):
    if n in S: return S[n]
    for i in FIinc(n):
        S[i] = i-1
    for p in range(2, isqrt(n)+1):
        if S[p] == S[p-1]: continue
        for v in FIdec(n):
            if v < p*p: break
            S[v] = S[v] - S[v//p] + S[p-1]
    return S[n]

N = 10**13          
lucy(N)                                                    

primes = seg_sieve(isqrt(N))

def countSignature(sig: list[int], x: int):
    def rec(i,j,x,rem):
        if i == len(sig) - 1:
            w = iroot(x,sig[i])
            return max(0, S[w] - j)
        t = 0
        for k in range(j,len(primes)):
            if primes[k]**rem > x: break
            t += rec(i+1, k+1, x//primes[k]**sig[i], rem-sig[i])
        return t
    return rec(0, 0, x, sum(sig))

def dfs(l):
    rv = countSignature(l, N)
    if rv == 0: return 0
    for i in range(l[-1], 0, -1):
        rv += dfs(l + [i])
    return rv

out = 0
for i in range(1, N.bit_length()):
    out += dfs([i])
print(out + 1)