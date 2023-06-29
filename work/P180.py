from math import gcd
from math import sqrt
def add(a,b):
    n = a[0]*b[1]+b[0]*a[1]
    d = b[1]*a[1]
    g = gcd(n,d)
    return (n//g, d//g)

def s(x,y,z):
    return add(add(x,y),z)

def reduce(a):
    return add(a,(0,1))

def isroot(n):
    return int(sqrt(n)) - sqrt(n) == 0

def multiply(a,b):
    n = a[0]*b[0]
    d = a[1]*b[1]
    g = gcd(n,d)
    return (n//g, d//g)
    
def inv(inp):
    return (inp[1], inp[0])

def f1(a,b):
    new = add(a,b)
    return reduce(new)

def f2(a,b):
    a = multiply(a,a)
    b = multiply(b,b)
    new = add(a,b)
    if not isroot(new[0]) or not isroot(new[1]):
        return False
    return reduce((int(sqrt(new[0])), int(sqrt(new[1]))))

def invf1(a,b):
    new = f1(inv(a),inv(b))
    return reduce(inv(new))

def invf2(a,b):
    new = f2(inv(a),inv(b))
    if new == False: return False
    return reduce(inv(new))

order = 35
rpfl = []
for denom in range(1,order+1):
    for num in range(1,denom):
        if gcd(num,denom) == 1:
            rpfl.append((num,denom))

sollist = set()

for x in rpfl:
    for y in rpfl:
        s1 = f1(x,y)
        s2 = f2(x,y)
        s3 = invf1(x,y)
        s4 = invf2(x,y)
        if s1 in rpfl:
            sollist.add(s(x,y,s1))
        if s3 in rpfl:
            sollist.add(s(x,y,s3))
        if s2 != False:
            if s2 in rpfl:
                sollist.add(s(x,y,s2))
        if s4 != False:
            if s4 in rpfl:
                sollist.add(s(x,y,s4))

uniquesols = list(sollist)
t = uniquesols.pop(0)
for n in uniquesols:
    t = add(t,n)
print(t[0] + t[1])