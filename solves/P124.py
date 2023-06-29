import math
def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return primes
thing = sieve(110000)
primes = []
for i in range(len(thing)):
    if thing[i] != 0: primes.append(thing[i])

def radn(n):
    rv = 1
    i = 0
    
    while primes[i]<=n:
        if n%primes[i] == 0: rv=rv*primes[i]
        i+=1
    return rv

print(radn(2))

def sort(listed, index):
    listed.sort(key = lambda x: x[index])
    return listed

thing = []
size = 100000
for i in range(1,size+1):
    thing.append([i,radn(i)])

thing = sort(thing,1)
print(thing[9999])
print(thing[10000])
print(thing[10001])

