from math import gcd, isqrt

def rep(x, n):
    rv = 0
    for a in range(1, n+1):
        if x % a == 0 and x//a <= n:
            rv += 1
    return rv 

def bf_d0(n):
    rv = 0
    for i in range(1, isqrt(n)+1):
        if n%i == 0:
            rv += 2
    return rv - (1 if isqrt(n)*isqrt(n) == n else 0)

def bf_d1(n):
    rv = 0
    for i in range(1, isqrt(n)+1):
        if n%i == 0:
            rv += i + n//i
    return rv - (isqrt(n) if isqrt(n)*isqrt(n) == n else 0)

def bf_S(n):
    rv = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            rv += bf_d1(i*j)
            print(i*j)
    return rv

def t1(n):
    rv = 0
    for i in range(1, n*n+1):
        rv += rep(i, n)*bf_d1(i)
    return rv

def t2(n):
    rv = 0
    for i in range(1, n+1):
        rv += bf_d1(i)*bf_d0(i)
    for i in range(n+1, n*n+1):
        rv += bf_d1(i)*rep(i, n)
    return rv

print(t2(3))