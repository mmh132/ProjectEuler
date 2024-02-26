from math import isqrt

def sieve(n):
    S = 10**5
    primes, oprimes = [], []
    rt = isqrt(n)
    
    isp = [1]*(rt + 1)
    for i in range(2, rt + 1):
        if isp[i]:
            primes.append(i)
            for k in range(i*i, rt, i):
                isp[k] = 0
    
    for k in range(n//S):
        block = [1] * S
        start = k*S
        for p in primes:
            i = (start + p - 1) // p
            for j in range(max(i, p)*p - start, S, p):
                block[j] = 0
        if k == 0:
            block[0] = 0
            block[1] = 0

        for i in range(S):
            if start + i > n: break
            if block[i]:
                oprimes.append(start + i)
    
    return primes + oprimes

def ntomask(n):
    mask = 0
    while n:
        update = 1 << n%10
        if mask & update: return -1
        mask += update
        n//=10
    if mask&1: return -1
    return mask >> 1

primes = sieve(10**9)
print("done")
pms = [0]*(1 << 9)
sms = [1] + [0]*(1 << 9)

for p in primes:
    m = ntomask(p)
    if m > -1:
        pms[m] += 1

for i in range(2**9):
    osms = sms.copy()
    for j in range(2**9):
        if not i&j:
            sms[i + j] += pms[i]*osms[j]

print(sms[2**9 - 1])



