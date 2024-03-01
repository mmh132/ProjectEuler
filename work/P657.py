from math import comb
MOD = 10**9 + 7
def S2(n, k):
    rv = 0
    for i in range(k + 1):
        rv += (-1) ** (k-i) * comb(k, i) * pow(i, n)
    return rv

def gs(b, l):
    if b == 0: return 0
    if b == 1: return l
    return b*(pow(b, l, MOD) - 1) * pow(b-1, -1, MOD) % MOD

N, K = 10**12, 10**7

f = [1,1]
for i in range(2, K+1):
    f.append((f[-1]*i) % MOD)

finv = [pow(f[-1], -1, MOD)]
k = K
while k>0:
    finv.append((finv[-1]*k) % MOD)
    k -= 1
finv.reverse()

def comb(n, k):
    if k < 0 or k > n: return 0
    return (f[n]*finv[n-k]*finv[k]) % MOD

def I(k, n):
    rv = 1
    for i in range(k):
        rv += (-1) ** (k-i+1) * comb(k, i) * gs(i, n)
        rv %= MOD
    return rv

print(I(10**7, 10**12))
