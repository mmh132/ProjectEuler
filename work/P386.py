

from math import isqrt, log
from functools import cache
from sympy.ntheory import sqrt_mod
from PEutil import sieve

N = 10**14

# gaussian integers with norm <= N
# inside the quarter plane a > 0 and b >= 0

primes = []
isc = [0] * (N + 1)
lpf = [0] * (N + 1)

lpf[1] = 1
for i in range(2, N + 1):
    if not isc[i]:
        primes.append(i)
        lpf[i] = i
    for p in primes:
        if i * p > N: break
        lpf[i*p] = p
        isc[i*p] = 1

def coeff(n):

    factors = {}
    while n != 1:
        l = lpf[n]
        if l in factors: factors[l] += 1
        else: factors[l] = 1
        n = n // lpf[n]
    
    

