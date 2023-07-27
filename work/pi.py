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


def pi(n):
    S = dict()
    for i in FIinc(n):
        S[i] = i-1
    for p in range(2, isqrt(n)+1):
        if S[p] == S[p-1]: continue
        for v in FIdec(n):
            if v < p*p: break
            S[v] = S[v] - S[v//p] + S[p-1]
    return S[n]

print(pi(10**11))