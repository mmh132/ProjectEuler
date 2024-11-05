from functools import cache
from math import comb

N = 10**15


@cache
def fac(n): return 1 if n < 1 else n * fac(n - 1)

@cache
def comb(n, k):
    if n == k or k == 0: return 1
    if k > n: return 0
    return comb(n-1, k) + comb(n-1, k-1)


# m * c choose c, c, c, ... c (m times)
def mf(m, c):
    rv = 1
    for i in range(c, m*c + 1, c):
        rv *= comb(i, c)  
    return rv

# burnsides lemma 
def f(m, n):
    if n == 1: return fac(m-1)
    rv = 0
    for i in range(1, n + 1):
        if n % i: continue
        # c is the number of cycles in the permutation pi_i (rotate by i)
        c = n//i 
        # ways to choose colors for the cycles
        rv += mf(m, c)
        print(rv)
    return rv // (m) // (n) 

f(2, 3)

# i, j = 2, 1
# rv = 0
# while f(i, j) < N:
#     while f(i, j) < N:
#         rv += f(i, j)
#         #print(i, j, "->", f(i, j))
#         j += 1
#     j = 1
#     i += 1
# print(rv)