from math import sqrt
from math import factorial
def choose(n, k):
    return factorial(n)//(factorial(n-k)*factorial(k))
    
def isprime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0: return False
    return True
def mul(l):
    rv = 1
    for i in l: rv*=i 
    return rv
primes = [i for i in range(2, 101) if isprime(i)]
print(primes)
cap = 10**16
founds = []
def recfind(nwant, sidx, prod):
    if nwant == 0:
        if prod<cap:
            founds.append(prod)
        return
    if prod * mul([primes[i] for i in range(sidx, min(sidx+nwant, 25))]) > cap: 
        return 
    for i in range(sidx, 25):
        recfind(nwant-1, i+1, prod*primes[i])
    return 
n = 0
x = 1
for i in range(4, 20):
    if i != 4:
        x = choose(i, 4) - choose(i-1, 4)
    founds = []
    recfind(i, 0, 1)
    for k in founds:
        n += pow(-1, i)*(cap//k)*int(x)
print(n)