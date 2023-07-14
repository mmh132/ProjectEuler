
from math import gcd


def isqrt(x):
    if x == 1: return 1
    a = x >> 1
    b = x
    while a < b:
        c = (a + x//a) >> 1
        a,b = c,a
    return b

def sumdiv(n):
    s = 0 
    for i in range(1, isqrt(n)+1):
        if n%i == 0:
            s += n//i + i
    if isqrt(n)*isqrt(n) == n:
        s -= isqrt(n)
    return s

def quot(n):
    x = sumdiv(n)
    d = gcd(n,x)
    return (x//d, n//d)

def bf(n):
    print(1)
    for i in range(1, n+1):
        x = quot(i)
        if x[1] == 2 and x[0]&1:
            print(i)

print("here")
print(sumdiv(24))
print(bf(100000))



