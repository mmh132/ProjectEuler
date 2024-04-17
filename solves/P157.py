from math import gcd, isqrt

def divs(n):
    rv = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            rv += 2
    if isqrt(n) * isqrt(n) == n:
        rv -= 1
    return rv

def sol(n):
    rv = 0
    for tp in range(0, 2*n + 1):
        for fp in range(0, 2*n + 1):
            a, b = 2**tp * 5**fp + 10**n, 2**(2*n-tp) * 5**(2*n-fp) + 10**n
            rv += divs(gcd(a, b))
    return (rv + (n+2)*(n+1))//2

print(sum([sol(i) for i in range(1, 10)]))
