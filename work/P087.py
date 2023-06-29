def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return primes
asdf = sieve(7071)
primes = []
for i in range(len(asdf)):
    if asdf[i] != 0:
        primes.append(asdf[i])
total = [0]
max = 50000000
found = []
def recbuild(currval, currpow, max):
    if currpow == 1:
        if currval<max:
           
                total[0]+=1
                
        print(total)
    else:
        i=0
        stor = currval+primes[i]**currpow
        while stor<max and i<len(primes)-1:
            recbuild(currval+primes[i]**currpow,currpow-1,max)
            i+=1
            stor = currval+primes[i]**currpow
recbuild(0,4,max)
print(total)
