def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return primes
def iscircular(n):
    for i in range(0,len(str(n))):
        if int(str(n)[i:]+str(n)[:i]) not in primeset:
            return False
    return True

firstset = sieve(1000000)
primeset = []
for i in range(len(firstset)):
    if firstset[i] != 0:
        primeset.append(firstset[i])
sum = 0
for i in range(len(primeset)):
    if iscircular(primeset[i]):
        print(primeset[i])
        sum+=1
print(sum)

