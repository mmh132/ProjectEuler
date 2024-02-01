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
            #print(i*j)
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

def ds(n):
    rv = 0
    for i in range(1, isqrt(n) + 1):
        rv += (n//i)*i
        rv += (n//i)*(n//i + 1) // 2
    return rv - isqrt(n)*isqrt(n)*(isqrt(n) + 1) // 2


for i in range(1, 10):
    print(ds(i)**2, bf_S(i), ds(i)**2 - bf_S(i))

for i in range(2, 15):
    for j in range(i, 15):
        print(i, j, bf_d1(i)*bf_d1(j), bf_d1(i*j), bf_d1(i)*bf_d1(j) - bf_d1(i*j))