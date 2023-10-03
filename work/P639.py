from math import comb, isqrt
import time
#from util.prime import FIdec, FIinc
from functools import cache as ccc
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
# def sumpow(n, exp):
#         rv = 0
#         if n > exp:
#             for i in range(1, exp+1):
#                 for j in range(i):
#                     rv += pow(-1, j)*pow(i-j, exp)*comb(n+exp-i+1, n-i)*comb(exp+1, j)
#                     rv %= MOD
#         return rv
# tp = 0
# s = time.time()
# for i in FIinc(10**12):
#     tp += sumpow(i, 50)
#     tp %= MOD
# print(tp, time.time() - s)
    
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
    #print(spow)
    #do powerful number sieving
    stk = [(1,1,0)]
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
    def h(p, e):
        out = 0
        if e > 1:
            out -= (pow(p, k) - 1)*pow(p,k)
        return 1 if e == 0 else out%MOD
    def powerfulnumberext(n):
        while stk:
            c = stk.pop(0)
            nn, hn, i= c[0], c[1], c[2]
            if i == len(primes): 
                yield (nn, hn)
                continue
            stk.append((nn, hn, i+1))
            p, e = primes[i], 2
            while nn*p**e <= n:
                stk.append((nn*p**e, hn*h(p,e), i+1))
                e += 1
    rv = 0
    for ii in powerfulnumberext(n):
        rv += ii[1]*spow[n//ii[0]]
        rv %= MOD
    return rv % MOD

print(S(100, 1))
print(sum(S(10**8, i) for i in range(1, 4)) % MOD)
