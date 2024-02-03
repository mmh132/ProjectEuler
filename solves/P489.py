from sympy.ntheory.residue_ntheory import nthroot_mod as nthrootmod
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

def G(a, b):
    d = udivs(divs(a*a), divs(a**6 + 27*b*b))
    m = (0,0)
    for k in d:
        if k < m[0]: continue
        valids = nthrootmod(-b, 3, k, True)
        if isinstance(valids, int): valids = [valids]
        for i in valids:
            if (pow(i+a, 3, k) + b) % k == 0:
                m = (k, i)
                break
    return m[1]

m, n = 18, 1900
rv = 0
for i in range(1, m+1):
    print(i)
    for j in range(1, n+1):
        rv += G(i, j)
print(rv)

        
    