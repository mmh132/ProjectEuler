def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return primes
thing = sieve(10000)
primes = []
for i in range(len(thing)):
    if thing[i] != 0: primes.append(thing[i])
def ways(n, idx):
    if n == 0: return 1
    if n<0: return 0
    a = 0
    while primes[a]<n: a+=1
    rv = 0
    for i in range(idx, a+1): rv += ways(n-primes[i], i)
    return rv
i = 10
n = ways(i,0)
while n<5000:
    i+=1
    n=ways(i,0)
    print(n)
print(i)