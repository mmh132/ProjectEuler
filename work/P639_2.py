from math import comb, isqrt
import time
from functools import cache as ccc
import sys
sys.setrecursionlimit(10000000)
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

N = 10**8
MOD = 10**9 + 7
   
def S(n, k):
    #brute force the first sqrt n values
    spow = {1: 1}
    for i in range(2, isqrt(n)+1):
        spow[i] = (spow[i-1] + pow(i,k,MOD)) % MOD
    print("done1")
    #print(spow)
    #use closed form for harder to compute values
    for i in FIdec(n):
        if i < isqrt(n)+1:
            break
        inn = 0
        for ii in range(1, k+1):
            for jj in range(ii):
                inn += pow(-1, jj)*pow(ii-jj, k)*comb(i+k-ii+1, i-ii)*comb(k+1, jj)
                inn %= MOD
        spow[i] = inn
    print("done2")
    #print(spow)
    #do powerful number sieving
    primes = []
    rt = isqrt(n)
    sieve = [1]*(rt+1)
    for i in range(2, isqrt(rt) + 1):
        if not sieve[i]:
            continue
        for z in range(i+i, rt+1, i):
            sieve[z] = 0
    for i in range(2, len(sieve)):
        if sieve[i] == 1:
            primes.append(i)
    print("sievedone")
    def h(p, e):
        out = 0
        if e > 1:
            out -= (pow(p, k) - 1)*pow(p,k)
        return 1 if e == 0 else out%MOD
    def rec(pp, hn, i):
        if i == len(primes):
            return hn * spow[n//pp] % MOD
        rv = rec(pp, hn, i+1)
        exp, prime = 2, primes[i]
        while pp*prime**exp <= n:
            rv += rec(pp*prime**exp, hn*h(prime,exp), i+1)
            rv %= MOD
            exp += 1
        return rv
    return rec(1,1,0) % MOD

print(S(100, 1))
print(sum(S(10**12, i) for i in range(1, 4)) % MOD)