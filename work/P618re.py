from functools import cache
import sys
sys.setrecursionlimit(100000)
N, MOD = 24, 10**9
f = [0,1]
while len(f) < N+1:
    f.append(f[-1] + f[-2])
print(f)
N2 = f[-1]
    
p = [0,0] + [1]*(f[-1]+ 1)
for i in range(2, len(p)):
    if p[i]: 
        for j in range(i+i, len(p), i):
            p[j] = 0

primes = [i for i in range(2, len(p)) if p[i]]
print(primes)

@cache
def dp(s, i):
    if s == 0: return 1
    if i == len(primes) or primes[i] > s:
        return 0
    rv = 0
    cur_p = primes[i]
    xx = 1
    for j in range(s//cur_p+1):
        rv += xx*dp(s-cur_p*j, i+1)
        xx = (xx*cur_p) % MOD
        rv %= MOD
    return rv

print(dp(5, 0))

currow = [1] + [0]*N2
newrow = [0]*(N2 + 1)
for i in range(len(primes)):
    cur_p = primes[i]
    xx = 1
    for j in range(N2//cur_p):
        for k in range(N2 - cur_p*j):
            newrow[k] += xx*currow[]