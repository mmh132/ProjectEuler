from math import log
def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x!=0]
def C(b,e):
    cap = e*log(b)
    #print(int(cap/log(2)))
    ps = sieve(int(cap/log(2)))
    t = 0
    for ai in range(len(ps)):
        a = ps[ai]
        for bi in range(ai+1,len(ps)):
            b = ps[bi]
            if a*log(b) + b*log(a) > cap:
                break
            else:
                t+=1
    return t
print(C(800800,800800))

    