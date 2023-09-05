from math import comb
from functools import cache 
def f(a, b, m):
    rv = 0
    for n in range(3, min(a, b)+1, 3):
        aa = (a-n)//2
        bb = (b-n)//2
        if (a-n)%2 == 1 or (b-n)%2 == 1: continue
        if aa > 0 or bb > 0:
            rv += 2*comb(aa + bb, aa)*comb(2*n + aa + bb - 1, aa + bb - 1)
            rv %= m
        else: 
            rv += 2
            rv %= m
    return rv
print(f(3,11,1234567891))
print(f(15,15,1234567891))


MOD = 1234567891
@cache
def bruteforce(a,b,c,m,n):
    if m == 0 and n == 0:
        return 1 if a == 1 and b == 2 and c == 3 else 0
    rv = 0
    if m > 0:
        rv += bruteforce(b,a,c,m-1,n)
    if n > 0:
        rv += bruteforce(a,c,b,m,n-1)
    return rv % MOD

print(bruteforce(1,2,3,3,11))
print(bruteforce(1,2,3,15,15))