from math import sqrt, gcd
def add(a,b):
    rv = (a[0]*b[1] + b[0]*a[1], a[1]*b[1])
    g = gcd(rv[0],rv[1])
    return (rv[0]//g, rv[1]//g)


def isprime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0: return False
    return True
prime = [False, False] + [isprime(i) for i in range(2,501)]


def dp()