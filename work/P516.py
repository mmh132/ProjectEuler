from PrimeUtil import MillerRabin64

def buildhammings(n):
    hammings = set()
    p2, p3, p5 = 0,0,0
    while (2**p2)*(3**p3)*(5**p5) <= n:
        while (2**p2)*(3**p3)*(5**p5) <= n:
            while (2**p2)*(3**p3)*(5**p5) <= n:
                hammings.add((2**p2)*(3**p3)*(5**p5))
                p5 += 1
            p5 = 0
            p3 += 1
        p3 = 0
        p2 += 1
    return len(hammings)

N = 10**12
ret = [0]
hams = buildhammings(N)
niceprimes = set()
for i in hams:
    if MillerRabin64(i+1):
        niceprimes.add(i+1)

founds = []
def recfind(sidx, prod):
    if prod<N:
        founds.append(prod)
    else:
        return
    for i in range(sidx, 25):
        recfind(i+1, prod*niceprimes[i])
    return 

def recrun2(n):
    
            