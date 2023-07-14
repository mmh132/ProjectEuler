from math import gcd
from totientsum import totientsum
def bf(n):
    s = 0
    for k in range(1, n+1):
        for i in range(1, k+1):
            s += i//gcd(i,k)
    return s

def bfnew(n):
    s = 0
    for i in range(1, n+1):
        for k in range(i, n+1):
            s += i//gcd(k,i)
    return s
print(bf(100))
print(bfnew(100))

def bftotient(n):
    if n == 1: return 1
    return sum(1 if gcd(x,n) == 1 else 0 for x in range(1, n))

def new(n):
    rv = 0
    for d in range(1, n+1):
        if n%d == 0:
            rv += (d)*bftotient(d)//2
    return rv

def newsn(n):
    rv = n
    for i in range(1, n+1):
        rv += new(i)
    return rv

def newagain(n):
    rv = n
    orv = n
    for i in range(1, n+1):
        rv += (bftotient(i)*(i))*(n//i)
        orv += bftotient(i)*n*(n//i//2)
    return rv//2

def run3(n):
    def ff(n):
        return n*n
    def gg(n):
        rv = n
        for i in range(2, n+1):
            if n%i == 0: n//=i; rv *= -1
            if n%i == 0: rv = 0
        return rv
    ret = 0
    for i in range(1, n+1):
        if n%i == 0:
            ret += gg(n//i)*ff(i)
    return ret

def run4(n):
    rv = n
    for i in range(1, n+1):
        rv += run3(i)*(n//i)
    return rv//2


print(new(10))
print(bftotient(45))
print(newsn(100))
print(newagain(100))
print(run4(100))