from math import gcd, isqrt

def tri(n):
    return n * (n + 1) // 2

def bfsum(x, n):
    rv = 0
    for i in range(1, n + 1):
        if gcd(x, i) == 1:
            rv += i
    return rv

def bfct(x, n):
    rv = 0
    for i in range(1, n + 1):
        if gcd(x, i) == 1:
            rv += 1
    return rv

print(bfsum(15, 100))
print(tri(100) - 5*tri(100 // 5) - 3*tri(100//3) + 15*tri(100//15))