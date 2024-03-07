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

MOD = 1001961001

def row(k):
    primes = []
    i = 2
    while len(primes) <= k:
        if isp(i): primes.append(i)
        i += 1
    dpold = [0] + [-1]*(k-1)
    dpnew = [0]*k
    for n in range(primes[k]):
        for r in range(k):
            dpnew[r] = max((dpold[(r + i) % k] + primes[i]) % MOD if dpold[(r+i)%k] > -1 else -1 for i in range(k)) % MOD
        dpold = dpnew.copy()
        dpnew = [0]*k
        print(n)
    return dpold[0]

print(row(7000))