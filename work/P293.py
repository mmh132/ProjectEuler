from PrimeUtil import MillerRabin64
import math
def isPrime(n):
    if n>10000:
        return MillerRabin64(n)
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0: return False
        return True
def nextPrime(n):
    rv = n+1
    while not isPrime(rv): rv += 1
    return rv
def find(n):
    return nextPrime(n)-n

all = []
def rb(cprime, n, cap):
    all.append(n)
    exp = 1
    while n*cprime**exp < cap:
        rb(nextPrime(cprime), n*cprime**exp, cap)
        exp+=1
    return

cap = 10**9
rb(2,1,cap)
uset = set()
for i in all:
    uset.add(find(i))
print(uset)
print(sum(uset)-1)