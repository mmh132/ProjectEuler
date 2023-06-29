from math import sqrt
def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x != 0]
def squarefreesub(n):
    psqs = [x**2 for x in sieve(int(sqrt(n)))]
    tot = 0
    for i in range(len(psqs)):
        tot += n//psqs[i]
    for i in range(len(psqs)):
        for k in range(i+1, len(psqs)):
            if psqs[i]*psqs[k]>n: break
            tot-= n//(psqs[i]*psqs[k])       
    print(n-tot)
print(squarefreesub(12))
