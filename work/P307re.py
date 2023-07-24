from math import factorial as fac

def choose(n, a, b, c):
    return fac(n)//fac(a)//fac(b)//fac(c)

def p(k, n):
    x = 0
    for c in range(k//2 + 1):
        b = k-2*c
        a = n-c-b
        x += choose(n, a,b,c)*fac(k)
    return 1-x/pow(n, k)

print(p(3,7))