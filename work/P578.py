from math import isqrt
import time
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
    return S[n]
x = time.time()
print(lucy(10**13))
print(time.time() - x)