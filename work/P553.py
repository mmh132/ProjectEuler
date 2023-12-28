# #bF(n) = R'(n) - sum of F(k)R'(n-k)
# from math import comb
# def R(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     x = 2**(2**n-1)-1
#     for m in range(n):
#         x -= comb(n, m)*R(m)
#     return x

# def 
# print(R(4))
import sys
sys.setrecursionlimit(100000)
n = 10**4
mod = 10**9 + 7

m = dict()
def comb(n, k):
    if k <= 0 or k >= n: return 1
    if (n,k) in m: return m[(n,k)]
    x = comb(n-1,k-1) + comb(n-1,k)
    x %= mod
    m[(n,k)] = x
    return x

r = [0, 1]
for i in range(n):
    r.append((2*(r[-1]+1)*(r[-1]+1) - 1)%mod)

R = [0]*(n+1)
for i in range(1, n+1):
    R[i] = r[i]
    for k in range(i):
        R[i] -= R[k]*comb(i,k)
        R[i] %= mod
    R[i] += mod

cache = dict()
def f(n, k):
    if (n,k) in cache: return cache[(n,k)]
    if n == 0: return 0
    x = 0
    if k == 1: 
        x = R[n]
        for i in range(1, n):
            x -= f(i, 1)*R[n-i]*comb(n-1,i-1)
            x%= mod
    else:
        for i in range(0, n-k+2):
            x += f(n-i, k-1)*f(i, 1)*comb(n-1,i-1)
            x %= mod
    cache[(n,k)] = x
    return x

def c(n, k):
    x = 0
    for i in range(1, n+1):
        x += f(i, k)*comb(n, i)
        x %= mod
    return x
print(R[2])
print(c(n, 10)%mod)