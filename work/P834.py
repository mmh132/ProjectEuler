from math import isqrt
def divs(n):
    rv = set()
    for i in range(1, isqrt(n) + 1):
        if n%i == 0:
            rv.add(i)
            rv.add(n//i)
    return rv

def udivs(a, b):
    rv = set()
    for x in a:
        for y in b:
            rv.add(x*y)
    return rv

def T(n):
    rv = 0
    for i in udivs(divs(n), divs(n-1)):
        if i > n:
            m = i-n
            if ((m+1)*n + m*(m+1)//2) % (m+n) == 0:
                rv += m
    return rv

def U(n):
    rv = 3
    for i in range(3, n+1):
        if not i % 10000: print(100*i/n)
        rv += T(i)
    return rv - 3

print(U(100))