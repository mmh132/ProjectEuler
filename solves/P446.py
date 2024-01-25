from math import isqrt

def bffac(n):
    rv = []
    p = 2
    while p <= isqrt(n):
        e = 0
        while n%p == 0:
            n //= p
            e += 1
        if e:
            rv.append((p, e))
        p += 1
    if n > 1:
        rv.append((n, 1))
    return rv

def unionfacs(f1, f2):
    f1.sort()
    f2.sort()
    rv = []
    while len(f1) and len(f2):
        if f1[0][0] < f2[0][0]:
            rv.append(f1.pop(0))
        elif f2[0][0] < f1[0][0]:
            rv.append(f2.pop(0))
        else:
            p, e = f1.pop(0)
            e += f2.pop(0)[1]
            rv.append((p, e))
    if len(f1):
        rv += f1
    if len(f2):
        rv += f2
    return rv

N = 10**7

facs = []
for _ in range(N+1): facs.append([])
fncsieve = [0] + [i*i+1 for i in range(1, N+1)]

