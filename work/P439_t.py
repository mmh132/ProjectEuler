from math import gcd

def divs(n):
    for i in range(1, n+1):
        if not n%i:
            yield i

#return sum d(i)d(j) for i, j <= n
def g(n):
    rv = 0
    for i in range(1, n+1):
        rv += i*(n//i)
    return rv**2

def sigma(n, k):
    rv = 0
    for i in range(1, n+1):
        if not n%i: 
            rv += i**k
    return rv

#sum u*v for u|g, v|g and u < v
def err(g):
    if g == 1: return g
    return (sigma(g, 1)**2 - sigma(g, 2))//2

def bf_f(n):
    rv = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            rv += sigma(i*j, 1)
    return rv

def bf_f_2(n):
    rv = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            d = gcd(i, j)
            ip, jp = i//d, j//d
            x = sigma(ip, 1)*sigma(jp, 1)
            if gcd(d, ip) > 1 or gcd(d, jp) > 1:
                x *= err(d)
                x = sigma(i, 1)*sigma(j, 1) - sigma(i*j, 1)
            else:
                x *= (sigma(d, 1)**2 - sigma(d**2, 1))
                #x = sigma(i, 1)*sigma(j, 1) - sigma(i*j, 1)
            x= sigma(i, 1)*sigma(j, 1) - x
            if sigma(i*j, 1) != x:
                print(i, j) 
            rv += x
    return rv
#sum d(i)d(j) for all i, j coprime
def bf_g_cop(n):
    rv = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if gcd(i, j) == 1:
                rv += sigma(i,1)*sigma(j, 1)
    return rv

def f(n):
    rv = g(n)
    for d in range(2, n+1):
        rv -= bf_g_cop(n//d)*err(d)
    return rv

for i in range(50, 50):
    print(f(i), bf_f(i), bf_f_2(i), i)

def test(i, j):
    x = sigma(i, 1)*sigma(j, 1)
    rv = 0
    d = gcd(i, j)
    for z in divs(d):
        rv += z*sigma(i*j//z//z, 1)
    return (x, rv)

print(test(2*3*2, 2*3*3))