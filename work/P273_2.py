from math import sqrt
def isprime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(1,150) if i%4 == 1 and isprime(i)]
print(primes)
print(2**(len(primes)))

def findsquarerep(p):
    for a in range(1, p):
        for b in range(a+1, p):
            if a**2 + b**2 == p:
                return (a,b)

psq = [findsquarerep(i) for i in primes]
print(psq)