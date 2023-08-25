from functools import cache
MOD = 10**9 + 7
@cache
def bf(n, k):
    if n == 0: return 1
    return sum(bf(i//k, k) for i in range(n+1))
dn = dict()
@cache
def nf(n, k):
    if n == 0: return 1
    dn[n] = 1
    rv = 0
    for i in range(n//k):
        rv += k*nf(i, k)
    rv += (n - (n//k)*k + 1)*nf(n//k, k)
    return rv % MOD
print(nf(10**4, 2))
print(len(dn))