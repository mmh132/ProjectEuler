from math import log
def isqrt(x):
    if x == 1: return 1
    a = x >> 1
    b = x
    while a < b:
        c = (a + x//a) >> 1
        a,b = c,a
    return b

def fenwickAdd(t, i, k):
    while i < len(t):
        t[i] += k
        i = i | (i+1)
    return t

def fenwickAsk(t, i):
    rv = 0
    while i >= 0:
        rv += t[i]
        i = (i & (i+1)) - 1
    return rv

def toFenwick(t):
    rv = [0]*len(t)
    for i, k in enumerate(t):
        rv = fenwickAdd(rv, i, k)
    return rv

def lucyFenwick(x):
    s = dict()
    y = round(0.35*pow(x, 1.5)/pow(log(x), 1.5))
    y = max(isqrt(x) + 1, y)
    if x <= 10000:
        y = int(x)
    
    rawSieve = [1]*(y+1)
    sieve = toFenwick([1]*(y+1))
    sieve = fenwickAdd(sieve, 0, 0)
    sieve = fenwickAdd(sieve, 1, 0)