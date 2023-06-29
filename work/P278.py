from math import sqrt
def isp(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(2, 5000) if isp(i)]


def f(p, q, r):
    rv = p*p*q*r
    rv -= p*q
    rv -= p*r
    rv -= r*q
    return rv

s = 0
for id1 in range(len(primes)):
    for id2 in range(id1 + 1, len(primes)):
        for id3 in range(id2 + 1, len(primes)):
            s += f(primes[id1], primes[id2], primes[id3])
print(s)