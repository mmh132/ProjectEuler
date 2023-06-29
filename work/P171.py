import time
start_time = time.time()
from math import gcd
from math import factorial as fac
def sumperms(thing):
    if len(thing) == 0: return 0
    if len(thing) == 1: return thing[0]
    thing = sorted(thing)
    absnum = [1]
    numref = [thing[0]]
    uniquenums = 1
    for i in range(len(thing)-1):
        if thing[i] == thing[i+1]: absnum[-1]+=1
        else: absnum.append(1); uniquenums+=1; numref.append(thing[i+1])
    perms = fac(sum(absnum))
    for i in range(len(absnum)):
        perms = perms//fac(absnum[i])
    rv = 0
    onedigit = 0
    div = gcd(*absnum)
    for i in range(len(absnum)):
        absnum[i] = absnum[i]//div
    perms = perms // sum(absnum)
    for i in range(len(absnum)):
        absnum[i]*=perms
    for i in range(len(numref)):
        onedigit += numref[i]*(absnum[i])
    for i in range(len(thing)):
        rv+=onedigit*(10**i)
    return rv
die = []
def choosesetsrep(cfrom, nchoose, out):
    if nchoose == 0:
        die.append(out)
    else:
        storein = cfrom[:]
        storeout = out[:]
        for i in range(len(cfrom)):
            storeout.append(cfrom[i])
            choosesetsrep(storein[i:],nchoose-1,storeout)
            storeout = out[:]
squares = []
i = 1
while i**2 < 20*9**2:
    squares.append(i**2)
    i+=1
digsq = []
for i in range(0,10):
    digsq.append(i**2)
def sumdigsquares(list):
    rv = 0
    for i in range(len(list)):
        rv += digsq[list[i]]
    return rv
choosesetsrep(list(range(10)),20,[])
tot = 0
for i in range(len(die)):
    if sumdigsquares(die[i]) in squares:
        tot += sumperms(die[i])
print(str(int(tot) % 10**9))
print("--- %s seconds ---" % (time.time() - start_time))