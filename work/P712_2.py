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

def sum_omega(n):
    rv = 0
    #lucy calcs
    S = dict()
    for i in FIinc(n):
        S[i] = i-1
    for p in range(2, isqrt(n) + 1):
        if S[p] == S[p-1]: continue
        for v in FIdec(n):
            if v < p*p: break
            S[v] -= (S[v//p] - S[p-1])
    print("here")
    #small primes
    for i in range(2, isqrt(n) + 1):
        if S[i] == S[i-1]: continue
        x = i
        while x <= n:
            rv += n//x
            x *= i

    #large primes
    for i in range(1, isqrt(n)):
        rv += (S[n//(i)] - S[n//(i+1)])*(i)
    
    return rv

