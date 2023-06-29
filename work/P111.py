from PrimeUtil import MillerRabin64

primes = []
for i in range(10**8, 10**9):
    if MillerRabin64(i):
        primes.append(i)
print("done")