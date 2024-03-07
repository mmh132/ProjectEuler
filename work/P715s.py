from math import isqrt, gcd
from functools import cache

MOD = 10**9 + 7

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

def lucy(n, e):
    def spow(n, e):
        if e == 0: return n
        if e == 1: return n*(n+1)//2
        if e == 3: return (n*(n+1)//2 % MOD) ** 2
        return -1
    S = dict()
    for i in FIinc(n):
        S[i] = (spow(i, e) - 1) % MOD
    for p in range(2, isqrt(n)+1):
        if S[p] == S[p-1]: continue
        for v in FIdec(n):
            if v < p*p: break
            S[v] = (S[v] - (p**e)*(S[v//p] - S[p-1])) % MOD
    return S

def lucyAP(n, k):
    cop, ci = [], [-1]*k
    for i in range(1, k):
        if gcd(i, k) == 1:
            cop.append(i)
            ci[i] = len(cop)-1
    
    piss = [{1:0} for _ in range(len(cop))]
    for i in range(len(cop)):
        for v in FIinc(n):
            piss[i][v] = (v - cop[i] + k) // k
            if i == 0: piss[i][v] -= 1
    
    inv = [0,1]
    for i in range(2, k):
        inv.append((k - k//i * inv[k%i]) % k)

    for p in range(2, isqrt(n) + 1):
        if gcd(p, k) - 1: continue
        if not any(piss[i][p] > piss[i][p-1] for i in range(len(cop))): continue

        for v in FIdec(n):
            if v < p*p: break
            for i in range(len(cop)):
                idx = ci[(cop[i]*inv[p % k]) % k]
                elim = piss[idx][v//p] - piss[idx][p-1]
                piss[i][v] -= elim
    
    return piss

N = 10**12
rt = isqrt(N)
p = [0,0] + [1]*(rt-1)
for i in range(2, isqrt(rt) + 1):
    p[i*i::i] = [0]*((rt - i*i)//i + 1)

primes = [1] + [i for i in range(2, rt + 1) if p[i]]

def mess(n, f, fp):

    @cache
    def dp(x, k):
        rv = fp[x] - fp[primes[k-1]] 
        for i in range(k, len(primes)):
            c, p_i = 1, primes[i]
            while p_i**(c + 1) <= x:
                rv += f(p_i, c)*dp(x//p_i**c, i + 1) + f(p_i, c+1)
                rv %= MOD
                c += 1
        #print("x", x, k, rv)
        return rv
    
    return dp(n, 1) + 1

F_p = lucy(N, 3)

weird = lucyAP(N, 4)
for i in F_p:
    F_p[i] += -weird[0][i] + weird[1][i]
    F_p[i] %= MOD

tf = lambda p, e: (pow(p, 3*(e-1))*(p*p*p + (1 if p % 4 == 3 else -1)) % MOD if p > 2 else pow(2, 3*e)) if e > 0 else 1
print("here")
print(mess(N, tf, F_p))