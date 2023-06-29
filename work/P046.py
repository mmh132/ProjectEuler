def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x != 0]
primes = sieve(100000)
twicesquares = [2*i**2 for i in range(1,1000)]
def isgold(n):
    if n in primes: return True
    for a in primes:
        if a > n: break
        if n-a in twicesquares:
            return True
    return False
i = 3
while isgold(i):
    i+=2
print(i)