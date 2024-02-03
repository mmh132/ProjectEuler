N, K, MOD = 10**16, 10**8, 10**9+7

f = [1,1]
for i in range(2, K+1):
    f.append((f[-1]*i) % MOD)

finv = [pow(f[-1], -1, MOD)]
k = K
while k>0:
    finv.append((finv[-1]*k) % MOD)
    k -= 1
finv.reverse()

def A(n, k):
    rv = 0
    for x in range(k//2 + 1):
        rv += f[K]*finv[x]*finv[x]*finv[k-2*x]*pow(2, (k-2*x)*n//k, MOD) 
        rv %= MOD
    return rv

<<<<<<< Updated upstream
print(A(N, K))
=======
print(A(N, K))
>>>>>>> Stashed changes
