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

S = dict()
def rpi(n):
    if n in S: return S[n]
    for i in FIinc(n):
        S[i] = i-1
    for p in range(2, isqrt(n)+1):
        if S[p] == S[p-1]: continue
        for v in FIdec(n):
            if v < p*p: break
            S[v] = S[v] - S[v//p] + S[p-1]
    return S[n]
rpi(10**12)
def pi(n):
    return rpi(n)

def lsieve(n):
    p = [1]*(n+1)
    for i in range(2, n+1):
        if not p[i]: continue
        for k in range(i+i, n+1, i):
            p[k] = 0
    return p

def s1(n):
    s = 0
    p = lsieve(int(pow(n, 1/2)))
    for p1 in range(2, int(pow(n, 1/3)) + 1):
        if not p[p1]: continue
        for p2 in range(p1+1, int(pow(n, 1/2)) + 1):
            if not p[p2]: continue 
            x = pi(n//(p1*p2)) - pi(p2)
            if x > 0:
                s += x
    return s

def s2(n):
    s = 0
    p = lsieve(int(pow(n, 1/3)))
    for p1 in range(2,int(pow(n, 1/3)) + 1):
        if not p[p1]: continue
        cs = s
        l = n//(p1*p1*p1)
        s += pi(l)
        if l >= p1:
            s -= 1
    return s

def s3(n):
    return pi(int(pow(n, 1/7)))

def f(n): 
    a,b,c = s1(n), s2(n), s3(n)
    print(a,b,c)
    return a+b+c

print(f(10**12))
            

