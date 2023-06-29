from math import sqrt
def factorn(n):
    facs = set()
    for i in range(1, n+1):
        if n%i == 0:
            facs.add(i)
    return facs

def checkten(n):
    while n%5 == 0:
        n//=5
    while n%2 == 0:
        n//=2
    return n == 1

def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x != 0]

def check(prime):
    for i in factorn(prime-1):
        if pow(10, i, prime) == 1 and checkten(i):
            return True
    return False

s = 0
primes = sieve(100000)
for i in primes:
    if not check(i):
        s += i
print(s+3)
# 3 is a special case, because i am making the assumption that the prime is not 9, so I dont have
#to care about the div by 9

