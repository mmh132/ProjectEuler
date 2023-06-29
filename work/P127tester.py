import time
def factorsieve(n):
    blank = []
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == []:
            rv[i].append(i)
            for k in range(i+i,len(rv),i):
                rv[k].append(i)
    return rv
t2 = time.time()
size = 50000
indices = []
for i in range(size+1):indices.append(0)
def product(t):
    t=list(t)
    rv = 1
    for i in range(len(t)):
        rv=rv*t[i]
    return rv
def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return primes
stor = sieve(size)
primes = []
for i in range(len(stor)):
    if stor[i] != 0: primes.append(stor[i])
def primefactorn(n):
    i = 0
    pf = []
    while n!=1:
        while n%primes[i]==0:
            n=n//primes[i]
            if primes[i] not in pf: pf.append(primes[i])
        i+=1
    return set(pf)
primefactorz = [[1,{1},1]]
k = set()
prod = int()
for i in range(2,size+1):
    k=primefactorn(i)
    prod = product(k)
    if prod != i or list(k)[0] == i: 
        primefactorz.append([i,k,prod])
        indices[i] = len(primefactorz)-1
print("--- %s seconds ---" % (time.time() - t2))

t1 = time.time()
factorsieve(50000)
print("--- %s seconds ---" % (time.time() - t1))