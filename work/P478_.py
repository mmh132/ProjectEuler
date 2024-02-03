from functools import cache

N, MOD = 10**1, 11**8

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

@cache
def M(n):
    rv = pow(n+1, 3, MOD) - 1
    la = 1
    for i in FIinc(n):
        if i == la: continue
        rv = (rv - (i-la)*M(n//i)) % MOD
        la = i
    return rv % MOD

#a > b
@cache
def M2(n):
    rv = n*(n+1)*(2*n+1)//6
    la = 1
    for i in FIinc(n):
        if i == la: continue
        rv = (rv - (i-la)*M2(n//i)) % MOD
        la = i
    return rv % MOD

#a=b
@cache
def M3(n):
    rv = n*(n+1)//2
    la = 1
    for i in FIinc(n):
        if i == la: continue
        rv = (rv - (i-la)*M2(n//i)) % MOD
        la = i
    return rv % MOD

def attempt(n):
    eq = M3(n)
    gr = M2(n)
    m = M(n)
    
    rv = pow(2, m) - 1
    
    err = 0
    err += 3 * (pow(2, eq + eq + gr) - 1)
    err += 3 * (pow(2, eq + gr + gr) - 1)
    
    err -= 3 * 3 * (pow(2, eq + gr) - 1)
    err -= 3 * 2 * (pow(2, eq) - 1)
    err -= 3 * 2 * (pow(2, gr) - 1)
    
    print(err)
    
    return rv - err

print(attempt(1))