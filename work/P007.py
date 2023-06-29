from math import sqrt

def sieve(n):
    primes = [1]*(n+1)
    for i in range(2, int(sqrt(n))+1):
        if primes[i]: 
            for k in range(i+i, n+1, i):
                primes[k] = 0
    return primes


primes = sieve(2*10**6)
foundCount = 0
for i in range(2,len(primes)):
    if primes[i]:
        if foundCount == 100000:
            print(i)
            break
        else: 
            foundCount += 1
