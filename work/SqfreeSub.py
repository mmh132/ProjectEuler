from math import sqrt
def mob(n):
    primes = [1]*(n+1)
    mobius = [1]*(n+1)
    for i in range(2, n+1):
        if primes[i]:
            mobius[i] *= -1
            for k in range(i+i, n+1, i):
                mobius[k] *= -1
                primes[k] = 0
            for k in range(i**2, n+1, i**2):
                mobius[k] = 0
    return mobius

def sqfree(n):
    moby = mob(int(sqrt(n)) + 1)
    t = 0
    for i in range(1, len(moby)):
        t += moby[i]*(n//i**2)
    return t

print(sqfree(2**50))