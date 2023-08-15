from math import comb, isqrt
import time
from itertools import cache
N = 10**8
MOD = 10**9 + 7

@cache
def sumpow(n, exp):
    rv = 0
    if n > exp:
        for i in range(1, exp+1):
            for j in range(i):
                rv += pow(-1, j)*pow(i-j, exp)*comb(n+exp-i+1, n-i)*comb(exp+1, j)
    else:
        for i in range(1,n+1):
            rv += pow(i, exp)
    return rv
