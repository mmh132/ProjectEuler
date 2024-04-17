from math import isqrt

N = 10**6
N *= 2
p = [0,0] + [1]*(N-1)
for i in range(2, isqrt(N) + 1):
    p[i*i::i] = [0]*((N - i*i)//i + 1)
primes = [i for i in range(5, N + 1) if p[i]]
N //= 2


rv = 0
for i in range(len(primes)):
    p1, p2 = primes[i], primes[i + 1]
    if p1 > N: break
    x = 10**len(str(p1))
    rv += (p1*pow(p2, -1, x) % x) * p2

print(rv)