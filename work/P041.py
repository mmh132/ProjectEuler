def isndigital(n):
    size = len(str(n))
    for i in range(1,size+1):
        if str(i) not in str(n):
            return False
    return True
def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return primes
stuff = sieve(10**8)
primes = []
for i in range(len(stuff)):
    if stuff[i] != 0 and len(str(stuff[i]))==7:
        primes.append(stuff[i])

for i in range(len(primes)):
    if isndigital(primes[i]):
        print(primes[i])