from functools import cache
N, MOD = 10**1, 11**8

def FIinc(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield la
        i = la + 1
        
def FIdec(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield n//la
        i = la + 1

cmp, mu, primes = [0]*(N+1), [0]*(N+1), []
mu[1] = 1  
for i in range(2, N+1):
    if not cmp[i]:
        primes.append(i)
        mu[i] = -1
    for j in primes:
        idx = i*j
        if idx > N: break
        cmp[idx] = 1
        if i%j == 0:
            mu[idx] = 0
        else:
            mu[idx] = mu[i]*-1

print([i for i in FIinc(1)])
print([i for i in FIinc(2)])

MOD = 10**9+7

@cache
def M(n):
    rv = pow(n+1, 3, MOD) - 1
    la = 1
    for i in FIinc(n):
        if i == la: continue
        rv = (rv - (i-la)*M(n//i)) % MOD
        la = i
    return rv % MOD

print(M(1), M(2))
print(M(100))
