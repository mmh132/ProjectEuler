from functools import cache
from math import isqrt

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

def it(n):
    for i in range(1, isqrt(n)+1):
        yield i*i

@cache
def g(u):
    if u == 1: return 1
    if u == 0: return 0
    l = [g(u-i) for i in it(u) if i <=u]
    return mex(set(l))

N = 10**4

vals = [0]*100
for i in range(0, N+1):
    vals[g(i)] += 1

def dp(layer, pxor):
    if layer == 0: return 1 if pxor == 0 else 0
    rv = 0
    for i in range(len(vals)):
        rv += dp(layer-1, pxor ^ i)*vals[i]
    return rv

x = dp(3, 0)   

#print(x//6, x)

x -= vals[0]*6

x -= vals[0]*(vals[0]-1)*3

x = x//6

x += vals[0]

x += vals[0]*(vals[0]-1)

#print(x)
