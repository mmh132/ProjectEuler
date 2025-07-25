from math import isqrt, log
from functools import cache
from sympy.ntheory import sqrt_mod
from PEutil import sieve

N = 1000      

rt = int(N)

primes = []
isc = [0] * (rt + 1)
lpf = [0] * (rt + 1)

lpf[1] = 1
for i in range(2, rt + 1):
    if not isc[i]:
        primes.append(i)
        lpf[i] = i
    for p in primes:
        if i * p > rt: break
        lpf[i*p] = p
        isc[i*p] = 1

#solves a^2 + b^2 = p 
def solve(p):
    r0 = sqrt_mod(-1, p)
    r1 = p % r0

    if r0 > p//2: r0 = p - r0

    while r0 > isqrt(p):

        r0, r1 = r1, r0 % r1
    
    return (r0, isqrt(p-r0*r0))

def val(a, b):
    oldr, r = a, b
    olds, s = 1, 0
    oldt, t = 0, 1

    while r != 0: 
        q = oldr // r
        oldr, r = r, oldr - q*r
        olds, s = s, olds - q*s
        oldt, t = t, oldt - q*t
    
    return (olds, oldt) if oldr == 1 else (0, 0)

def factor(n):
    rv = []
    for p in primes:
        if n == 1: return rv
        if n%p == 0:
            rv.append(p)
            n //= p

            if n%p==0 or p%4!=1:
                return []
    return rv

def mul(a, b, c, d):
    return (a*c-b*d, a*d+b*c)

def normalize(a, b):
    for x, y in [(a, b), (-a, -b), (-b, a), (b, -a)]:
        if x > 0 and y > 0:
            return (x, y)
    return None

L = rt
solns = {}
for p in primes:
    if p%4 == 1:
        solns[p] = solve(p)

rv = 0
for i in range(1, L + 1):
    ps = factor(i)
    if ps:
        #print("here" , i)
        toa2 = 0
        fail = []
        suc = []
        for mask in range(2**(len(ps) - 1)):

            # find corresponding a+bi for the mask
            ap, bp = 1, 0
            for idx, p in enumerate(ps):
                nap, bap = solns[p]
                ap, bp = mul(ap, bp, nap, bap * (-1 if (mask >> idx)&1 else 1))
            ap, bp = mul(ap, bp, ap, bp)
            ap, bp = normalize(ap, bp)

            # find coeffs
            y, z= val(ap, bp)

            x = abs(ap * z - bp * y)
            ox = i*i - x

            toa = 0
            
            if N - x >= 0:
                toa += (N - x) // (i * i) + 1
            if N - ox >= 0:
                toa += (N - ox) // (i * i) + 1
            
            toa2 += toa
            if toa == 0:
                fail.append((ap, bp))
            else: 
                suc.append((ap, bp))

        if toa2 == 0: print("fail", i, len(ps), "failed:", fail, "didnt:", suc)
        else: print("SUCC", i, len(ps), "failed:", fail, "didnt:", suc)
        rv += -toa2 * (-1) ** len(ps)

print(N - rv)

# rv = 0
# stk = [(1, 0)]

# for p in primes:
#     if p % 4 == 3: continue

#     z, y = solve(p)

#     nstk = []
#     for a, b in stk:
#         new = mul(a, b, z, y)
#         if val(*new) < N:
#             rv += 1
#             nstk.append(new)
    
#     stk += nstk

# print(rv)