<<<<<<< Updated upstream
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

print(len(sieve(10**9)))
=======
n = 100
dvs = [0]*(n + 1)
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        dvs[j] += 1
        dvs[j] %= 6
print(dvs)
ct = 0
for i in range(1, n + 1):
    if dvs[i] % 6 == 0:
        print(i)
        ct += 1
print(ct)

>>>>>>> Stashed changes
