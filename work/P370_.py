from math import gcd, isqrt


def bf(n):
    rv = 0
    for x in range(1, n):
        if 3*x*x > n: 
            break
        for y in range(x, n):
            if gcd(x, y) == 1 and y*y < x*(x + y):
                rv += n//(x*x + x*y + y*y)
            if x*x + x*y + y*y > n: break
    return rv

print(bf(10**6))