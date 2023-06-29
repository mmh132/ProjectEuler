def factorn(n):
    facs = set()
    for i in range(1, n+1):
        if n%i == 0:
            facs.add(i)
    return facs

def checkten(n):
    ctr5 = 0
    ctr2 = 0
    while n%5 == 0 and ctr5 < 9:
        n//=5
        ctr5+=1
    while n%2 == 0 and ctr2 < 9:
        n//=2
        ctr2+=1
    return n == 1

def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x != 0]

def check(prime):
    if prime == 3: return False
    for i in factorn(prime-1):
        if pow(10, i, prime) == 1 and checkten(i):
            return True
    return False


ctr = 0
s = 0
primes = sieve(200000)
for i in primes:
    if ctr > 39: break
    if check(i):
        s += i
        print(i)
        ctr += 1
print(s)