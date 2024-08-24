from functools import cache
from math import gcd

def ll(d):
    for i in range(2, d + 1):
        if d%i == 0:
            return i

def binexp(n):
    bs = list(bin(n)[2:])
    rv = 0
    while bs:
        if int(bs.pop(0)) > 0: rv += 1
        rv += 1
    return rv - 2

def t(e):
    rv = 0
    while e:
        if e&1:
            rv += 1
        rv += 1
        e >>= 1
    return rv

print(binexp(15))

def dp(vset, n, l, lpf):
    print(vset, n, l, lpf)
    if len(vset) >= l or max(vset)*2**(l-len(vset)) < n: 
        return l
    if n in vset: 
        return len(vset)
    vset = set(vset)
    rv = l
    moves = set()
    for i in vset: 
        for j in vset:
            moves.add(i + j)
    for i in moves:
        if i not in vset and i > max(vset):
            if (i > lpf and gcd(i, n) > 1) or i < lpf:
                vset.add(i)
                rv = min(rv, dp(tuple(sorted(list(vset))), n, l, lpf))
                vset.remove(i)
    return rv

i = 15
print(dp((1,), i, binexp(i), ll(i)))
# L = 200
# rv = 0
# for i in range(1, L + 1):

#     o = rv
#     rv += dp((1,), i, binexp(i), ll(i))
#     print(i, binexp(i), rv - o)
# print(rv)