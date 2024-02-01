from math import isqrt, gcd

def d(n):
    rv = set()
    p = 2
    while p < isqrt(n) + 1:
        e=0
        while not n%p:
            n//=p
            e+=1
        if e:
            rv.add((p, e))
        p += 1
    if n > 1:
        rv.add((n, 1))
    return rv

Y = 10**6
tot, cmp, primes = [0]*(Y+1), [0]*(Y+1), []
tot[1] = 1
for i in range(2, Y+1):
    if not cmp[i]:
        primes.append(i)
        tot[i] = i-1
    for j in primes:
        idx = i*j
        if idx > Y: break
        cmp[idx] = 1
        if i % j == 0:
            tot[idx] = tot[i] * j
        else:
            tot[idx] = tot[i] * (j - 1)

for i in range(2, Y+1):
    if (i-1) % (i-tot[i]) == 0 and cmp[i]:
        print(i, tot[i], i-tot[i], d(i), d(tot[i]), d(i-tot[i]))