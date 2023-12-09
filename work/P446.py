from math import gcd, isqrt
def pollards_p1(n, lim = 10**2):
    a = 2
    for j in range(2, lim):
        a = pow(a, j, n)
        if 1 < gcd(a-1, n) < n:
            return gcd(a-1, n)
    return -1
def factor(n):
    f = []
    for i in range(2, isqrt(n) + 1):
        while n%i==0:
            n//=i
            f.append(i)
    return (f + [n]) if n!= 1 else f

for i in range(1, 101):
    print(i, factor(i*i-2*i+2), factor(i*i+2*i+2))