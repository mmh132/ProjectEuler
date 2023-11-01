from math import isqrt, gcd
from functools import cache
#card {(x,y) | x^2 + y^2 <= n, x>y}
@cache
def f(n):
    rv = 0
    for x in range(1, isqrt(n) + 1):
        z = isqrt(n-x*x) - x + 1
        rv += z if z>0 else 0
    return rv

#card {(x,y) | x^2 + y^2 <= n, x>y, x and y odd}
@cache
def fodd(n):
    rv = 0
    for x in range(1, isqrt(n) + 1, 2):
        z = (isqrt(n-x*x)+1)//2 - (x+1)//2 +1
        rv += z if z>0 else 0
    return rv

def P(n):
    p = [1]*(isqrt(n) + 1)
    m = [1]*(isqrt(n) + 1)
    for i in range(2, isqrt(n)+1):
        if p[i]:
            m[i] *= -1
            for j in range(i+i, isqrt(n)+1, i):
                m[j]*=-1
                p[j] = 0
            for j in range(i**2, isqrt(n)+1, i**2):
                m[j] = 0
    rv = 0
    for i in range(1, isqrt(n) + 1):
        if i%10000 == 0: print(i/isqrt(n))
        rv += m[i]*f(n//(i*i))
    for i in range(1, isqrt(n) + 1, 2):
        if i%10001 == 0: print(i/isqrt(n))
        rv -= m[i]*fodd(n//(i*i))
    return rv

print(P(3141592653589793))






# def bruteforce(n):
#     rv = 0
#     for i in range(1, isqrt(n) + 1):
#         for k in range(i, n):
#             if i*i+k*k > n: break
#             if gcd(i,k) == 1:
#                 rv += 1
#     print(rv)
#     overct = 0
#     for i in range(1, isqrt(n) + 1, 2):
#         for k in range(i, n):
#             if i*i+k*k > n: break
#             if gcd(2*i,k) == 1:
#                 overct += 1
#     print(overct)
#     return rv-overct

# print(cp(10**6))
# print(bruteforce(10**6))

#card {(x,y) | x^2 + y^2 <= n, x>y, gcd(x,y) = 1, x and y odd}
# @cache
# def cpodd(n):
#     rv = fodd(n)
#     for k in range(3, isqrt(n) + 1, 2):
#         rv -= cpodd(n//(k*k))
#     return rv

# def Ptest(n):
#     return cp(n) - cpodd(n)

#card {(x,y) | x^2 + y^2 <= n, x>y, gcd(x,y) = 1}
# @cache
# def cp(n):
#     rv = f(n)
#     for k in range(2, isqrt(n) + 1):
#         rv -= cp(n//(k*k))
#     return rv