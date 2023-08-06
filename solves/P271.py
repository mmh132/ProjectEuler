from math import isqrt
from itertools import product

def crt(cg):
    m = 1
    for i in cg:
        m *= i[1]
    rv = 0
    for i in cg:
        a = i[0]
        m1 = m//i[1]
        n1 = pow(m1,-1,i[1])
        rv = (rv + a * m1 % m * n1) % m
    return rv

def isprime(n):
    for i in range(2,isqrt(n)+1):
        if n%i == 0: return False
    return True

bigmod = [i for i in range(2, 44) if isprime(i)]

def msq(n):
    rv = list()
    for i in range(1, n):
        if i**3 % n == 1:
            rv.append((i,n))
    print(len(rv),n)
    return rv

t = 0
for x in product(*[msq(n) for n in bigmod]):
    t += crt(x)
print(t-1)
