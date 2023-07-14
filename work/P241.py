from P379 import isqrt
from math import gcd

def sumdiv(n):
    s = 0 
    for i in range(1, isqrt(n)):
        s += n//i + i
    if isqrt(n)*isqrt(n) == n:
        s += isqrt(n)
    return s

def quot(n):
    x = sumdiv(n)
    d = gcd(n,x)
    return (x//d, n//d)

def bf(n):
    print(1)
    for i in range(1, n+1):
        print(i)
        x = quot(i)
        if x[1] == 2 and x[0]&1:
            print(i)

print(bf(10))



