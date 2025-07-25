from math import isqrt, log
from functools import cache
from sympy.ntheory import sqrt_mod
from PEutil import sieve

N = 10**14

# gaussian integers with norm <= N
# inside the quarter plane a > 0 and b >= 0
@cache
def g(n):
    rv = 0
    for a in range(isqrt(n) + 1):
        rv += isqrt(n - a*a)
    return rv


rt = isqrt(N)

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

def coeff(n):

    factors = {}
    while n != 1:
        l = lpf[n]
        if l in factors: factors[l] += 1
        else: factors[l] = 1
        n = n // lpf[n]
    
    rv = 1
    for p, e in factors.items():
        if p % 4 == 1:
            coeff = -2 if e == 1 else 1
            if e > 2: return 0
        elif p % 4 == 3:
            coeff = -1 
            if e != 2: return 0
        else: 
            coeff = -1
            if e != 1: return 0
        rv *= coeff
    return rv


rv = 0
for i in range(1, isqrt(N) + 1):
    
    rv += coeff(i) * g(N//i//i)

print(rv)



# # iterate through all numbers coprime to p and less than n
# def coprime(p, start, n):
#     pm = start % p
#     i = start
#     while i < n:
#         if pm != p:
#             yield i
#         i += 1
#         pm += 1
    


# mob = [1]*(isqrt(N)+1)
# prime = [1]*(isqrt(N)+1)
# for i in range(2, isqrt(N)+1):

#     if prime[i]:

#         if i == 2:

#             mob[i] *= -1
#             for j in range(i+i, isqrt(N)+1, i):
#                 mob[j] *= -1
#                 prime[j] = 0
#             for j in range(i**2, isqrt(N)+1, i**2):
#                 mob[j] = 0

#         if i % 4 == 1:

#             mob[i] *= -2
#             for j in range(i+i, isqrt(N)+1, i):
#                 mob[j] *= -2
#                 prime[j] = 0
#             for j in range(i**2, isqrt(N)+1, i**2):
#                 mob[j] = -mob[j]//2
#             for j in range(i ** 3, isqrt(N) + 1, i ** 3):
#                 mob[j] = 0

#         if i % 4 == 3:

#             # mob[i] *= 0
#             # sq = i*i
#             # for j in range(i+i, isqrt(N)+1, i):
#             #     mob[j] *= (-1 if j == sq else 0)
#             #     if j == sq: sq = sq + 2 * isqrt(sq) + 1
#             #     prime[j] = 0
#             for e in range(1, 100):
#                 for j in coprime(j, 1, isqrt(N) + 1):
#                     if j * i ** e > isqrt(N): break
#                     if j * i ** e == 45: print("here", j, i, e)
#                     mob[j * i ** e] *= (-1 if e == 2 else 0)
#                     prime[j] = 0


            





# #solves a^2 + b^2 = p 
# def solve(p):
#     r0 = sqrt_mod(-1, p)
#     r1 = p % r0

#     if r0 > p//2: r0 = p - r0

#     while r0 > isqrt(p):

#         r0, r1 = r1, r0 % r1
    
#     return (r0, isqrt(p-r0*r0))



# Z_primes = sieve(isqrt(N))[1:]

# C_primes = [(1, 1)]
# for p in Z_primes:
#     if p % 4 == 1:
#         a, b = solve(p)
#         Z_primes.append((a, b))
#         Z_primes.append((b, a))
#     else:
#         Z_primes.append((p, 0))

# stk = []
# for a, b in C_primes:
#     pass

# ---

# mob = [1]*(isqrt(N)+1)
# prime = [1]*(isqrt(N)+1)
# for i in range(2, isqrt(N)+1):

#     if prime[i]:

#         coeff = 2 if i % 4 == 1 else -1

#         mob[i] *= coeff
#         for j in range(i+i, isqrt(N)+1, i):
#             mob[j] *= coeff
#             prime[j] = 0
#         for j in range(i**2, isqrt(N)+1, i**2):
#             mob[j] = 0


# rv = 0
# for i in range(1, isqrt(N) + 1):
#     j = i
#     if i != 2: j = i*i
#     rv += mob[i] * g(N//j//j)
#     print(i, mob[i], g(N//j//j))
# print(rv)