from math import isqrt
from functools import cache
@cache
def gt(n):
    if n == 1: return 1
    rv = 1
    for i in range(2, isqrt(n)):
        if n%i == 0:
            rv += gt(i) + gt(n//i)
    return rv

print(gt(2*2*2*2*3))
print(gt(3*3*3*3*2))

def isprime(n):
    for i in range(2, isqrt(n) + 1):
        if n%i == 0: return False
    return True

# primes = [i for i in range(2,100) if isprime(i)]
# N = 10**16
# allforms = []
# def dp(cf, cmin):
#     print(cf, cmin)
#     allforms.append([cmin] + cf.copy())
#     np = primes[len(cf)]
#     i = 1
#     while cmin*np**i <= N and (len(cf) == 0 or i <= cf[-1]):
#         dp(cf + [i], cmin*np**i)
#         i += 1
# dp([], 1)
# x=0
# for i in allforms:
#     x += gt(i[0])
# print("done")

    