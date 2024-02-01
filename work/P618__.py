from math import isqrt
import time
t = time.time()
N, MOD = 24, 10**9

f = [0,1]
while len(f) < N + 1:
    f.append(f[-1] + f[-2])
N2 = f[-1]

p = [0,0] + [1]*(N2-1)
for i in range(2, isqrt(N2) + 1):
    p[i*i::i] = [0]*((N2 - i*i)//i + 1)

primes = [i for i in range(len(p)) if p[i]]

dpold = [1] + [0]*N2
dpnew = [0]*(N2 + 1)

for cp in primes:
    c, e = 1, 0
    while e < N2 + 1:
        for i in range(e, N2+1):
            dpnew[i] = (dpnew[i] + c*dpold[i-e]) % MOD
        e += cp
        c = (c*cp) % MOD
    dpold = dpnew.copy()
    dpnew = [0]*(N2 + 1)

print(dpold[8])
print(sum([dpold[f[i]] for i in range(2, N+1)]) % MOD)
print(time.time() - t)
            