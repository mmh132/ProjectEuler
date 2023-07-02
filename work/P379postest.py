from math import sqrt, gcd

def mob(n):
    primes = [1]*(n+1)
    mobius = [1]*(n+1)
    for i in range(2, n+1):
        if primes[i]:
            mobius[i] *= -1
            for k in range(i+i, n+1, i):
                mobius[k] *= -1
                primes[k] = 0
            for k in range(i**2, n+1, i**2):
                mobius[k] = 0
    return mobius

def isqrt(x):
    if x == 1: return 1
    a = x >> 1
    b = x
    while a < b:
        c = (a + x//a) >> 1
        a,b = c,a
    return b

def oH(n):
    s = 0
    for i in range(1, n+1):
        for j in range(1, min(n//i + 1, i + 1)):
            s += 1
    return s

def o2H(n):
    s = 0
    for i in range(1, n+1):
        s += min(n//i, i)
    return s

def o3H(n):
    s = isqrt(n)*(isqrt(n)+1) // 2
    for z in range(1, isqrt(n) + 1):
        if n//z != z:
            s += (n//z - n//(z+1))*(z)
    return s

def speedfalt(n):
    msieve = mob(isqrt(n))
    s = 0
    for k in range(1, isqrt(n) + 1):
        s += msieve[k]*o3H(n//(k*k))
    return s

def bf(n):
    s = 0
    for x in range(1, n+1):
        for y in range(1, x+1):
            if x*y//gcd(x,y) <= n:
                s += 1
    return s

def f(n):
    s = 0
    for i in range(1, n+1):
        for j in range(1, min(n//i + 1, i + 1)):
            if gcd(i,j) == 1:
                s += 1
    return s

def slowg(n):
    s = 0
    for d in range(1, n+1):
        a = f(n//d)
        b = speedfalt(n//d)
        if a != b:
            print(a,b,d,n//d)
        s += b
    return s

def altslowg(n):
    s = 0
    for d in range(1, isqrt(n) + 1):
        s += speedfalt(n//d)
    for z in range(1, isqrt(n) + 1):
        if n//z != z:
            s += (n//z - n//(z+1))*speedfalt(z)
    return s

print(altslowg(10**3))
print(slowg(10**3))
print(bf(10**3))

for i in range(1, 1000):
    c = o3H(10**4//i)
    a = o2H((10**4)//i)
    b = oH((10**4)//i)
   
    #print(a, b, c, i, 10**4//i)