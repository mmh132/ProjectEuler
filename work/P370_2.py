from math import gcd, isqrt, sqrt
from functools import cache
import time
def bf(n):
    rv = n//3
    for x in range(1, n):
        for y in range(x+1, n):
            if x*x + x*y + y*y <=n and y*y < x*(x+y):
                if gcd(x,y) == 1:
                    rv += n//(x*x + x*y + y*y)
            else:
                break
    return rv

print(bf(10**6))

@cache
def nogcd(n):
    if n < 3: return 0
    rv = 0
    for x in range(1, isqrt(n)):
        for y in range(x+1, int(0.5*(x + sqrt(5)*x)) + 1):
            if x*x + x*y + y*y <= n and y*y < x*(x+y):
                rv += n//(x*x+x*y+y*y)
            else:
                break
    return rv

def at3(n):
    rt = isqrt(n)
    m = [1]*(rt+1)
    p = [1]*(rt+1)
    for i in range(2, rt+1):
        if p[i]:
            m[i] *= -1
            for k in range(i+i, rt+1, i):
                m[k] *= -1
                p[k] = 0
            for k in range(i**2, rt+1, i**2):
                m[k] = 0
    #print("sieving done")
    rv = 0
    for i in range(1, rt+1):
        rv += m[i]*nogcd(n//i//i)
    return rv
        
def eval3(n):
    return at3(n) + n//3


print(eval3(10**9))

for i in range(3, 8):
    x = time.time()
    print(eval3(10**i))
    print(time.time() - x, "seconds")
