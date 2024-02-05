from functools import cache
from math import log2
# def log2(n):
#     rv = 0
#     while n&1 == 0: n>>=1; rv += 1
#     return rv

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

def it(n):
    for i in range(1, n):
        if n%i == 0: 
            yield i

print([i for i in it(24)])

@cache
def g(u):
    if u == 1: return 0
    l = [g(u-i) for i in it(u)]
    return mex(set(l))

for i in range(1, 100):
    print(g(i), i)

# def bf(n):
#     rv = n**3
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             for c in range(1, n+1):
#                 if g(a)^g(b)^g(c) == 0:
#                     rv -= 1
#     return rv

N, K, mod = 123456787654321, 3, 1234567890

#a or convolve b in nlogn, FWHT algorithm
def exp2(n, e):
    return (n//2**e - 1)//2 + 1
    
def xorconvolve(a, b):
    n = 0
    while (1 << n) < max(len(a), len(b)):
        n += 1
    while len(a) < (1 << n):
        a.append(0)
    while len(b) < (1 << n):
        b.append(0)
    
    c = [0]*((1<<n)+1)
    for ia, i in enumerate(a):
        for jb, j in enumerate(b):
            c[ia^jb] += i*j
            c[ia^jb] %= mod
    return c

# t = [exp2(N, i) for i in range(int(log2(N)) + 5)]
# print(pow(N, 3, mod) - xorconvolve(xorconvolve(t.copy(), t.copy()), t.copy())[0])