from math import isqrt, gcd
def is3p(n):
    x = 3
    while x < n:
        x *= 3
    return n==x

def sumdiv(n):
    rv = 0 
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            rv += n//i + i
    if n == isqrt(n)*isqrt(n): rv -= isqrt(n)
    return rv

def test(n):
    d = n//gcd(n, sumdiv(n))
    if is3p(d):
        return True
    return False

def T(n):
    rv = 0
    for i in range(1, n+1):
        if test(i):
            rv += i
            print(i)
    return rv

print(T(10**6))

    
