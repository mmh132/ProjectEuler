from math import gcd
def totient(n):
    rv = list(range(n+1))
    for i in range(2, n+1):
        if rv[i] != i: continue
        for k in range(i, n+1, i):
            rv[k]*= i-1
            rv[k]//= i
    return rv
def mobius(n):
    mob = [1]*(n+1)
    prime = [1]*(n+1)
    for i in range(2, n+1):
        if prime[i]:
            mob[i] *= -1
            for j in range(i+i, n+1, i):
                mob[j]*=-1
                prime[j] = 0
            for j in range(i**2, n+1, i**2):
                mob[j] = 0
    return mob

tot = totient(1000)
mu = mobius(1000)
def s1(n, m):
    rv = 0
    for i in range(1, n+1):
        if gcd(i, m) == 1:
            rv += tot[i]
    return rv

def s2(n, m):
    rv = 0
    for i in range(1, n+1):
        rv += tot[i]
    for d in range(2, m+1):
        if m%d == 0:
            rv -= mu[d]*s2(n//d, m)
    return rv

print(s1(100, 21))
print(s2(100, 21))
