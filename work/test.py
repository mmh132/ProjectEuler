from math import gcd, isqrt
def factors(i):
    k = 2
    r = set()
    while i > 1:
        while i % k == 0:
            i//=k
            r.add(k)
        k += 1
    return r
def f(i):
    t = 0
    for d in factors(i):
        t += 2**len(factors(d))
    return (t+1)//2

print(sum(f(i) for i in range(1, 1001)))

def g(n):

    s = 0
    for a in range(1, n+1):
        for b in range(1, n//a + 1):
            if gcd(a,b) == 1:
                s += n//(a*b)
    return (s+n)//2

print(g(1000))

def bff(n):
    s=0
    for a in range(1, n+1):
        for b in range(1, n//a + 1):
            if gcd(a,b) == 1:
                s += n//a//b
    return s

def bfh(n):
    s = 0
    for a in range(1, n+1):
        for b in range(1, n//a + 1):
            s += n//a//b
    return s




print(bfh(100))
print(sum(bff(100//i//i) for i in range(1, 11)))
