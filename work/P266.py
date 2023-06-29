from math import sqrt 
def isprime(n):
    return not True in [n%i == 0 for i in range(2, int(sqrt(n))+1)]
magicnum = 1
primes = [i for i in range(2, 191) if isprime(i)]
print(len(primes))
pprimes = 1
for i in primes: 
    pprimes *= i
root = int(sqrt(pprimes))
best = [1]
def rb(cIdx, p):
    if p > root:
        return
    if best[0] < p:
        best[0] = p
        print(best[0] % 10**16)
    for i in range(cIdx,42):
        rb(i+1, p*primes[i])
rb(0, 1)
print(best[0] % 10**16)