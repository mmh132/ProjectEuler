from math import isqrt, log
from bisect import bisect_left as bl
LIM = 190
p = [1]*(LIM+1)
for i in range(2, len(p)):
    for k in range(i+i, len(p), i):
        p[k] = 0
primes = [i for i in range(2, len(p)) if p[i] == 1]
pp = 1
for i in primes: pp *= i
prt = isqrt(pp)

a1, a2 = [], []
for i in range(len(primes)):
    if i < len(primes)//2:
        a1.append(primes[i])
    else:
        a2.append(primes[i])

print(a1, a2)

bs1, bs2 = [1], [1]
for a in a1:
    new = bs1.copy()
    for i in bs1:
        if a*i < isqrt(pp):
            new.append(a*i)
    bs1 = new.copy()

for a in a2:
    new = bs2.copy()
    for i in bs2:
        if a*i < isqrt(pp):
            new.append(a*i)
    bs2 = new.copy()

bs2.sort()
cb = 0
for v1 in bs1:
    target = prt//v1
    p = bl(bs2, target)
    if p == len(bs2) or (p < len(bs2) and bs2[p] != target):
        p = p-1
    if prt - bs2[p]*v1 < prt - cb and prt - bs2[p]*v1 >= 0:
        cb = bs2[p]*v1
print(cb % 10**16)


