from math import isqrt

N = 100

rt = isqrt(N)
primes, cmp, mu = [],[0]*(rt+1),[0]*(rt+1)
mu[1] = 1
for i in range(2, rt+1):
    if not cmp[i]:
        primes.append(i)
        mu[i] = -1
    for j in primes:
        idx = i*j
        if idx > rt: break
        cmp[idx] = True
        if i%j == 0:
            mu[idx] = 0
            break
        else:
            mu[idx] = mu[i]*-1

mem = dict()
def sqfree(n):
    if n in mem: return mem[n]
    rv = 0
    for i in range(1, isqrt(n) + 1):
        rv += mu[i]*(n//i//i)
    mem[n] = rv
    return rv



