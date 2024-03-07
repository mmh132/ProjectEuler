N, MOD = 12344321, 135707531

f = [1,1]
for i in range(2, N+1):
    f.append((f[-1]*i) % MOD)

finv = [pow(f[-1], -1, MOD)]
for k in range(N, 0, -1):
    finv.append((finv[-1]*k) % MOD)
finv.reverse()

rv, c = N*(N-1)*pow(N-1-1, N-1, MOD), N

def inv(x):
    return finv[x]*f[x-1]

for k in range(2, N-1):
    c = (c*(N-k+1)*inv(k)) % MOD
    rv = (rv + c*f[k-1]*pow(N-k-1,N-k,MOD)) % MOD

print(rv)