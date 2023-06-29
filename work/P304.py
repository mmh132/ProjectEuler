from Fibonacci import fib
from PrimeUtil import MillerRabin64


def nextprime(n):
    rv = n+1
    while not MillerRabin64(rv):
        rv +=1
    return rv

a = [-1, nextprime(10**14)]
for i in range(100000): a.append(nextprime(a[-1]))
print("here")

fseq = [fib(a[i], 1234567891011) for i in range(1,100001)]

print(sum(fseq) % 1234567891011)