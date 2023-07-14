from math import sqrt
def solve(n):
    primes = [1]*(int(n**(1/3))+1)
    sqfree = [1]*(int(n**(1/3))+1)
    for i in range(2, int(sqrt(len(primes))) + 1):
        if primes[i]:
            for k in range(i+i, len(primes), i):
                primes[k] = 0
            for k in range(i**2, len(primes), i**2):
                sqfree[k] = 0
    print(sqfree)
    rv = 0
    for i in range(2, len(sqfree)):
        rv += sqfree[i]*int(sqrt(n//(i*i*i)))
    return rv
print(solve(3*10**6))
