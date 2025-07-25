MOD = 10**9 + 7

N = 2

f = [1,1]
for i in range(2, N+1):
    f.append((f[-1]*i) % MOD)

finv = [pow(f[-1], -1, MOD)]
for k in range(N, 0, -1):
    finv.append((finv[-1]*k) % MOD)
finv.reverse()

def comb(n, k):
    if k > n or k < 0: return 0
    if n == k or k == 0: return 1
    return (f[n] * finv[k] * finv[n-k]) % MOD

rv = 0

for i in range(1, N + 1):
    rv += pow(-1, i - 1) * pow(2, N*(N - i - 1), MOD) * comb(N, i)
    rv %= MOD

print(rv)