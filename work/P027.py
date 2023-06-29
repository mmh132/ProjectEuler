def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x != 0]
primes = sieve(1000000)
best = 0
bs = [x for x in primes if x < 1000]
def test(a,b):
    n = 0
    thing = b
    while thing in primes:
        n+=1
        thing = n**2 + a*n + b
    return n
for b in bs:
    for a in range(-999,1000):
        if test(a,b) > best:
            best = test(a,b)
            print(a*b)


