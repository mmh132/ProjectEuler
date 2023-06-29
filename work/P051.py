primesize = 6
def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x != 0]
primes = [str(i) for i in sieve(10**primesize-1) if i > 10**(primesize-1)]
print(len(primes))


