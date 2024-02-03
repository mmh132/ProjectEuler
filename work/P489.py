from sympy.ntheory.residue_ntheory import nthroot_mod as nthrootmod
from math import isqrt 

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

def fac(n):
    rl = []
    p = 2
    while p < isqrt(n):
        while n%p == 0:
            n = n//p
            rl.append(p)
        p += 1
    if n>1: 
        rl.append(n)
    return n
        
def G(a,b):
    #factor a,b
    f = [3] + fac(a*a) + fac(a**6 + 27*b**2)
    f.sort()
        

def bs(l, target):
    def recurse(low, high):
        if abs(low-high) <= 1: 
            return low 
        mid = (low + high) // 2
        if l[mid] > target:
            return recurse(low, mid)
        else:
            return recurse(mid, high)
    return recurse(0, len(l) - 1)

x = [1,1,5,7,9,4,2,4,324,6,23,1,3]
x.sort()
print(bs(x, 6), x[bs(x, 6)])
            
     
print(nthrootmod(41, 3, 84))