from math import isqrt
from functools import cache

N = 10**16
rt = isqrt(N)

p = [0,0] + [1]*(rt-1)
for i in range(2, isqrt(rt) + 1):
    p[i*i::i] = [0]*((rt - i*i)//i + 1)

@cache
def f(n):
    rv = (n+3)//4 
    for k in range(3, isqrt(n) + 1, 2):
        rv -= f(n//(k*k))
    return rv

s = f(N)
for i in range(3, len(p), 4):
    if p[i]:
        s += f(N//(i*i))
print(s)