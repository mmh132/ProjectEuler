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
    rv = 0
    onedigit = 0
    for i in range(len(numref)):
        onedigit += numref[i]*(len(thing)-1)
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
for i in range(1,20):
    print("choosing " + str(i))
    choosesetsrep(digsq, i, [])
tot = 0
for i in range(len(die)):
    if i % 10 == 0: print(len(die)-i)
    if sum(die[i]) in squares:
        tot += sumperms(die[i])
print(tot)