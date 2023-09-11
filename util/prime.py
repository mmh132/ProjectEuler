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

def pi_lmo(n):
    v = isqrt(n)
    s = (v+1) // 2
    smalls = [(i + 1) // 2 for i in range(v+1)]
    roughs = [2 * i + 1 for i in range(s)]
    larges = [(n // ( 2 * i + 1) + 1) // 2 for i in range(s)]
    skip = [0] * (v+1)

    pc = 0
    for p in range(3, v+1, 2):
        if skip[p]: continue
        if p * p * p * p > n: break
        skip[p] = 1
        for i in range(p * p, v + 1, 2 * p):
            skip[i] = 1
        ns = 0
        for k in range(s):
            i = roughs[k]
            if skip[i]: continue
            if i*p <= v:
                x = larges[smalls[i*p] - pc]
            else:
                x = smalls[n//(i*p)]
            larges[ns] = larges[k] + pc - x
            roughs[ns] = i
            ns += 1
        for j in range(v // p, p - 1, -1):
            c = smalls[j] - pc
            for i in range(v, j*p-1, -1):
                smalls[i] -= c

    rv = larges[0] + (s + 2 * (pc-1))
    for l in range(1, s):
        q = roughs[l]
        m = n//q
        e = smalls[m//q] - pc
        if e<=l:
            break
        t = 0
        for r in roughs[l + 1 : e + 1]:
            t += smalls[m // r]
        rv += t - (e - l) * (pc + l - 1)
    return rv


def timef(f, inp):
    s = time.time()
    rv = f(inp)
    return (rv, time.time()-s)

print(timef(lucy, 10**9))
print(timef(pi_lmo, 10**9))
print(timef(lucyfen2, 10**9))
            
    
    
        
        
        
        
    
    