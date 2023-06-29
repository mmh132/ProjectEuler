size = 50000
import time

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
total = 0
numhits = 0
for a in range(len(primefactorz)):
    for b in range(a+1, len(primefactorz)):
        if primefactorz[a][0]+primefactorz[b][0]<size:
            if indices[primefactorz[a][0]+primefactorz[b][0]] != 0:
                if primefactorz[a][2]*primefactorz[b][2]*primefactorz[indices[primefactorz[a][0]+primefactorz[b][0]]][2]<primefactorz[a][0]+primefactorz[b][0]:
                    if primefactorz[a][1].intersection(primefactorz[b][1]) == set():
                        if primefactorz[indices[primefactorz[a][0]+primefactorz[b][0]]][1].intersection(primefactorz[b][1]) == set():
                            if primefactorz[a][1].intersection(primefactorz[indices[primefactorz[a][0]+primefactorz[b][0]]][1]) == set():
                                total += primefactorz[a][0]+primefactorz[b][0]
                                if primefactorz[a][2] == primefactorz[a][0] and len(list(primefactorz[a][1])) != 1: print(primefactorz[a][0])
                                if primefactorz[b][2] == primefactorz[b][0] and len(list(primefactorz[b][1])) != 1: print(primefactorz[b][0])
                                #print(primefactorz[a][0],primefactorz[b][0],primefactorz[a][0]+primefactorz[b][0])
                                numhits+=1
print(total)
print(numhits)

    

