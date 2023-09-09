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

def sieve(n):
    primes, s = [], [1]*(n+1)
    for i in range(2, isqrt(n) + 1):
        if not s[i]: continue
        for k in range(i*i, n+1, i):
            s[k] = 0
    for i in range(2, len(s)):
        if s[i]: primes.append(i)
    return primes

def boolsieve(n):
    rv = [1]*(n+1)
    for i in range(2, isqrt(n) + 1):
        if not rv[i]: continue
        for k in range(i*i, n + 1, i):
            rv[k] = 0
    return rv

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

#print(lucyfen(10**9)[10**9])              
    
def lucyfen2(n):
    y = int(n**(2/3))
    fen = [0]*(y+1)
    raw = [1]*(y+1)
    raw[0], raw[1] = 0,0
    S = dict()
    
    for i in range(y):
        fen[i] += 1
        r = i | (i+1)
        if r < y: fen[r] += fen[i]
        
    def fenadd(i, x):
        while i < y:
            fen[i] += x
            i = i | i+1
            
    def fensum(i):
        rv = 0
        while i>=0:
            rv += fen[i]
            i = (i & i+1) - 1 
        return rv
    
    fenadd(0,-1)
    fenadd(1,-1)
    
    for v in FIdec(n):
        if v > y:
            S[v] = v-1
            
    def eval(x):
        if x > y: return S[x]
        return fensum(x)

    for p in range(2, isqrt(n) + 1):
        if not raw[p]: continue
        for v in FIdec(n):
            if v <= y: break
            S[v] -= eval(v//p) - eval(p-1)
        for k in range(p+p, y+1, p):
            if raw[k]:
                raw[k] = 0
                fenadd(k, -1)
    
    return S[n]

s = time.time()
print(lucy(10**9))
print(time.time() - s)
s = time.time()
print(lucyfen2(10**9)) 
print(time.time() - s)


            
    
    
        
        
        
        
    
    