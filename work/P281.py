from math import factorial as fac, gcd

def mrot(m,n):
    x = fac(m*n)
    for i in range(m):
        x//=fac(n)
    print(m,n,x) 
    return x

def solve(m,n):
    rv = mrot(m,n)
    for k in range(m,m*n,m):
        rv += mrot(m, gcd(n,k))
    return rv//m//n

print(solve(4,4))