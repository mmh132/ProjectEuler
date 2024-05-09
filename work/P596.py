from math import isqrt

def so(n):
    rv = 0
    for i in range(1, isqrt(n) + 1):
        rv += (n//i) * i
        rv += (n//i) * (n//i + 1) // 2
        rv %= 10**9 + 7
    return rv - isqrt(n) * isqrt(n) * (isqrt(n) + 1) // 2

def T(r):
    return (8*so(r*r) - 32*so((r*r)//4) + 1) % (10 ** 9 + 7)

print(T(10**8))



