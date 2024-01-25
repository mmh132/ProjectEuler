from math import gcd
def f(n):
    rv = 0
    for a in range(1, n+1):
        for b in range(1, n//a + 1):
            if gcd(a,b) == 1:
                rv += 1
    return rv

def g(n):
    rv = 0
    for i in range(1, n+1):
        rv += f(n//i)
    return rv

print((g(10**6) + 10**6)//2)