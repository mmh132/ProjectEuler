from math import comb
from functools import cache

# def choose(n, k):
#     if k < 0 or k > n: return 0
#     return comb(n, k)

# def ksa(n, k, a):
#     rv = 0
#     l = n//a if a > 0 else 0
#     for i in range(l + 1):
#         rv += choose(n-i*a + k - a - 1, k - a - 1)
#     return rv

# print( ksa(4, 4, 3))
# print( ksa(2, 4, 3))
# print( ksa(2, 4, 4))

# print(ksa(4, 4, 2), ksa(2, 4, 2))

# x = 0
# x += ksa(4, 4, 2) * ksa(2, 4, 2) * choose(4, 2) 
# print(x)
# x -= ksa(4, 4, 3) * ksa(2, 4, 3) * choose(4, 3)
# print(x)
# x += ksa(4, 4, 4) * ksa(2, 4, 4) * choose(4, 4) 
# print(x)

def p(n, k):
    if k > n or k == 0: return 0
    if n == k: return 1
    return p(n-1, k-1) + p(n-k, k)

def q(n, k):
    return p(n-comb(k, 2), k)

print(q(8, 4), q(6, 4))

print(p(8, 4), p(6, 4))