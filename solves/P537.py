from math import isqrt, log

N, K, MOD = 20000, 20000, 1004535809

p = [0,0] + [1]*int(N*log(N) + N*log(log(N)) + 20000)
for i in range(2, isqrt(len(p))):
    if not i: continue 
    for j in range(i+i, len(p), i):
        p[j] = 0

for i in range(len(p)): p[i] += p[i-1]

pv = [0]*(N+1)
for i in range(1, len(p)):
    if p[i] > N: break
    pv[p[i]] += 1

def conv(a, b, n):
    c = [0]*(n+2)
    for idx1, v1 in enumerate(a):
        for idx2, v2 in enumerate(b):
            if idx1+idx2 > n+1:
                break
            c[idx1+idx2] += v1*v2
            c[idx1+idx2] %= MOD
    return c

pv[0] = 1

out = [1]
#binary exponentiation
while K:
    if K % 2 == 1:
        nout = conv(out.copy(), pv.copy(), N)
        out = nout.copy()
    npv = conv(pv.copy(), pv.copy(), N)
    pv = npv.copy()
    K //= 2

print(out[N])
