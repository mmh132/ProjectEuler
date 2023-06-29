primes = []
def isprime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
def nextPrime(n):
    for i in range(n+1,2*n+1):
        if isprime(i):
            return i
    return -1
n=1
for i in range(1000):
    n=nextPrime(n)
    primes.append(n)

print(primes)
