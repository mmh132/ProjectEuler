from math import gcd

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

def recrun(depth, n):
    if depth == 0: 
        return add((1,1), (1,n))
    return add((1,1), flip(add((1, 1), recrun(depth-1, n))))

s = 0
for i in range(1000):
    x = recrun(i, 2)
    if len(str(x[0])) > len(str(x[1])):
        s += 1

print(s)