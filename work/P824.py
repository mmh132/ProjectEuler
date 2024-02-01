from functools import cache
from math import comb
def bfrow(n, k):
    if k == 0: return 1
    @cache
    def dp(s, n, k):
        if n == -1 and k == 0 and s == False: 
            return 1
        if n < 0: 
            return 0
        if k == 0 and n == 0:
            return 1
        if s == True and (n == 1 and k == 1): 
            return 0
        return dp(s, n-1, k) + dp(s, n-2, k-1)
    return dp(True, n-2, k-1) + dp(False, n-1, k)

def fastrow(n, k):
    if k > n//2: return 0
    return n*comb(n-k, k)//(n-k)


def conv(a, b, lim):
    c = [0]*min(len(a) + len(b) - 1, lim)
    for ia, ca in enumerate(a):
        for ib, cb in enumerate(b):
            if ia+ib < len(c):
                c[ia + ib] += ca*cb
    return c

def bf(n, k):
    x = [fastrow(n, i) for i in range(k)]
    
    print(x)
    pw = n
    tp = [1]
    while pw:
        tp = conv(x.copy(), tp.copy(), k+2)
        pw -= 1
    return tp[k]

print(bf(4, 12))
print(bf(5, 12))
print(bf(6, 12))
print(bf(7, 12))
print(bf(8, 12))

        