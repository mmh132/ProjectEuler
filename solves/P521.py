from math import isqrt

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

def sumprimes(n):
    vals = dict()
    for i in FIinc(n):
        vals[i] = i*(i+1)//2 - 1
    for p in range(2, isqrt(n) + 1):
        if vals[p] == vals[p-1]: continue
        for v in FIdec(n):
            if v < p*p: break
            vals[v] -= p*(vals[v//p] - vals[p-1])
    return vals[n]

def final(n):
    rv = 0
    oldval = n

    S = dict()
    for i in FIinc(n):
        S[i] = i-1
    for p in range(2, isqrt(n) + 1):
        if S[p] == S[p-1]: continue
        for v in FIdec(n):
            if v < p*p: break
            S[v] -= (S[v//p] - S[p-1])
        rv += (oldval - S[n] + 1)*p
        oldval = S[n]
    rv += sumprimes(n) - sumprimes(isqrt(n))
    return rv

print((final(10**12) - 2) % 10**9)