from math import isqrt, gcd

def cop(a, b): return gcd(a, b) == 1

L = 120000

p = [1]*(L+1)
rs = [1]*(L+1)
for i in range(2, L + 1):
    if p[i]:
        for j in range(i, L + 1, i):
            rs[j] *= i
            p[j] = 0
        p[i] = 1

valids = []
r = []
for i in range(1, L + 1):
    if p[i] or rs[i] < i:
        valids.append(i)
        r.append(rs[i])

sc = 0
for i in range(len(valids)):
    if not i % 1000: print(100*i/len(valids))
    for j in range(len(valids)):
        a, b = valids[i], valids[j]
        c = a+b
        if not a < b < c < L: continue
        if not cop(a, b) or not cop(b, c) or not cop(a, c): continue
        if r[i]*r[j]*rs[c] < c:
            sc += c
print(sc)



