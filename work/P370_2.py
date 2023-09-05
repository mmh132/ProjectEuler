from math import gcd
from functools import cache
def bf(n):
    rv = n//3
    for x in range(1, n):
        for y in range(x+1, n):
            if x*x + x*y + y*y <=n and y*y < x*(x+y):
                if gcd(x,y) == 1:
                    rv += n//(x*x + x*y + y*y)
            else:
                break
    return rv

print(bf(10**6))


def all(n):
    rv = 0
    for x in range(1, n):
        for y in range(x+1, n):
            if x*x + x*y + y*y <= n and y*y < x*(x+y):
                rv += n//(x*x + x*y + y*y)
            else: 
                break
    return rv

@cache
def wewant(n):
    rv = all(n)
    for k in range(2, n):
        rv -= k*wewant(n//k)
    return rv
print(wewant(10**6))

# def bbf(n):
#     rv = 0
#     for a in range(1, n):
#         for b in range(a, n):
#             for c in range(b, n):
#                 if a+b+c > n: break
#                 if c >= a+b: break
#                 if b*b==a*c:
#                     print(a,b,c)
#                     rv += 1
#     return rv

# def alt(n):
#     rv = 0
#     for a in range(1, n):
#         for b in range(a, n):
#             if b*b % a == 0:
#                 if b*b//a < a + b: 
#                     if b*b//a + a + b <= n:
#                         rv += 1
#     return rv