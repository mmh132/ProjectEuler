def sieve(size):
    primes = list(range(2,size+1))
    for i in range(len(primes)):
        if primes[i] != 0:
            for j in range(i+primes[i],len(primes),primes[i]):
                primes[j] = 0
    return [x for x in primes if x != 0]
inset = sieve(5000)
coeffs = [0]*(sum(inset)+2)
cop = coeffs.copy()
o = sieve(len(coeffs)-2)
coeffs[0] = 1
for i in inset:
    cop = coeffs.copy()
    for k in range(len(coeffs)):
        if cop[k] != 0:
            coeffs[k+i] = (coeffs[k+i] + cop[k]) % 10**16
t = 0
for i in o: t += coeffs[i]
print(t%10**16)