from functools import cache as ccc
N,K,MOD = 10000, 10, 10**9+7
@ccc
def binom(n,m): return binom(n-1,m-1) + binom(n-1,m) if n>m>0 else 1

def f(n):
    rv = pow(2, 2**n-1, MOD)-1
    for i in range(n):
        rv -= f(i)*binom(n,i)
    return rv

print(f(2))
