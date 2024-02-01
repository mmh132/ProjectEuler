from math import isqrt
from functools import cache
import sys

sys.setrecursionlimit(1000000)
def isp(n):
    for i in range(2, isqrt(n) + 1):
        if not n%i: return False
    return True

def bf(k):
    primes = []
    i = 2
    while len(primes) <= k:
        if isp(i): primes.append(i)
        i += 1
    @cache
    def dp(r, n):
        if n == 0: return -1000000 if r else 0
        return max(dp((r + i) % k, n-1) + primes[i] for i in range(k))
    for i in range(primes[k]):
        dp(0, i)
    return dp(0, primes[k])

print(bf(10))

def sol(k):
    primes = []
    i = 2
    while len(primes) <= k:
        if isp(i): primes.append(i)
        i += 1
    