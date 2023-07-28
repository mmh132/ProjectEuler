from math import gcd, isqrt
#testing some small formulas
def d(n):
    s = -isqrt(n) if isqrt(n)*isqrt(n) == n else 0
    for i in range(1, isqrt(n)+1):
        if n%i == 0:
            s += n//i + i
    return s


def f(a):
    s = 0
    for b in range(1, a+1):
        if gcd(a, b) == 1:
            s += d(b)
    return s

#sum of d(a*b) for b in [1, a-1]
def S1(a):
    s = 0
    alts = 0
    for b in range(1, a+1):
        s += d(a*b)
        k = gcd(a,b)
        alts += d(a//k)*d(b//k)*d(k)*d(k)
    return s, alts
#same thing with extra formula
def S2(a):
    s = 0
    for k in range(1, a+1):
        if a%k == 0:
            s += d(a//k)*d(k*k)*f(a//k)
    return s

print(S1(10))
print(S2(10))

print(S1(20))
print(S2(20))