from math import gcd
from math import sqrt

def multiply(a,b):
    n = a[0]*b[0]
    d = a[1]*b[1]
    g = gcd(n,d)
    return (n//g, d//g)

def add(a,b):
    n = a[0]*b[1]+b[0]*a[1]
    d = b[1]*a[1]
    g = gcd(n,d)
    return (n//g, d//g)

def flip(f):
    return (f[1], f[0])

def bestbound(n, cap):
    if int(sqrt(n)) ** 2 == n:
        return 0
    
    sv = (n+1, n)
    ln = 0
    while sv[1] < cap:
        ln = sv[0]
        sv = add((1,1), flip(add((1, 1), sv)))
        print(sv)
    return ln

print(bestbound(13, 30))

#print(sum(bestbound(n, 10**12) for n in range(2, 100001)))