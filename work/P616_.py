from math import isqrt

N = 10**12
rt = isqrt(N)

p = [0,0] + [1]*(rt-1)
for i in range(2, isqrt(rt) + 1):
    p[i*i::i] = [0]*((rt - i*i)//i + 1)

primes, cmp = [], []
for i in range(2, rt + 1):
    if p[i]: primes.append(i)
    else: cmp.append(i)

rs = set()
for i in primes:
    if 2 ** i > N: break
    for c in cmp:
        if c ** i < N: 
            rs.add(c ** i)
        else: break
print(sum(rs) - 16)