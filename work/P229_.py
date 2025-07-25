from math import isqrt, log
from functools import cache
from sympy.ntheory import sqrt_mod
from PEutil import sieve

#solves a^2 + d * b^2 = m
def solve(d, m):
    r0 = sqrt_mod(-d, m)
    r1 = m % r0

    if r0 > m//2: r0 = m - r0

    while r0 > isqrt(m):

        r0, r1 = r1, r0 % r1
    
    return (r0, isqrt(m-r0*r0))