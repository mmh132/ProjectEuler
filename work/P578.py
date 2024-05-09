from math import isqrt
import time
\

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

print(lucy(10**10)[10**10])