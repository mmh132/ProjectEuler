import math
die = []
def choosesets(cfrom, nchoose, out):
    if nchoose == 0:
        die.append(out)
    else:
        storein = cfrom[:]
        storeout = out[:]
        for i in range(len(cfrom)):
            storein.pop(0)
            storeout.append(cfrom[i])
            choosesets(storein,nchoose-1,storeout)
            storeout = out[:]
def choose(cfrom, nchoose):
    choosesets(cfrom,nchoose,[])
    return die
def prod(list):
    rv = 1
    for i in range(len(list)): rv*= (list[i]-1)
    return rv
def f(turns):
    blank = []
    things = list(range(2,turns+2))
    blank = choose(things, turns - (math.floor(turns/2)+1))
    tot = 1 #start with identity, so 1
    for i in range(len(blank)): tot += prod(blank[i])
    for i in range(math.floor(turns/2)+2, turns):
        blank.clear()
        blank = choose(things, turns - i)
        for i in range(len(blank)): tot += prod(blank[i])
    return math.floor((tot/math.factorial(turns+1))**-1)
print(f(15))