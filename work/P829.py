import math
def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return primes
empty = sieve(31)
primes = []
for i in range(len(empty)): 
    if empty[i] != 0: primes.append(empty[i])
def prod(list):
    n = 1
    for i in range(len(list)): n*=list[i]
    return n
def doublefactorial(n):
    if n%2 == 1: 
        for i in range(1,n,2): n*=i
        return n
    else:
        for i in range(2,n,2): n*=i
        return n
def primefactorn(n):
    fac = []
    for i in range(2,32):
        while n%i == 0: n//=i; fac.append(i)
    return fac
def soln(n):
    facn = doublefactorial(n)
    minprimefacs = primefactorn(facn)
    num1 = 1
    num2 = prod(minprimefacs)
    print(num1)
    print(num2)
    bestdiff = 100000000000000000
    for i in range(len(minprimefacs)):
        if abs(num1*minprimefacs[i] - num2//minprimefacs[i]) < bestdiff:
            num1 *= minprimefacs[i]
            num2 = num2//minprimefacs[i]
            bestdiff = abs(num1-num2)
    print(num1)
    print(num2)
    return
soln(31)
    
