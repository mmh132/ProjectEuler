N = 10**7

primes = []
cmp = [0]*(N+1)
phi = [0]*(N+1)
phi[1] = 1
for i in range(2, N):
    if not cmp[i]:
        primes.append(i)
        phi[i] = i-1
    for j in primes:
        if i*j >= N: break
        cmp[i*j] = 1
        phi[i*j] = phi[i]*j - phi[i] if i%j else 0

bv, bi = 100, 0
for i in range(2, N):
    n, pn = i, phi[i]
    if sorted(str(n)) == sorted(str(pn)):
        if n/pn < bv:
            bv = n/pn
            bi = n

print(bi)