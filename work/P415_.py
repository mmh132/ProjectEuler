from math import gcd, isqrt
import time

start = time.time()

nottest = True
mod = 2*10**8
N = 10**11 
Y = int((N+1)**(2/3))

def FIinc(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield la
        i = la + 1
        
def FIdec(n):
    i, la = 1,0
    while i <= n:
        la = n//(n//i)
        yield n//la
        i = la + 1

def sumpow(n, k):
    if k == 0:
        return (n) % mod
    elif k == 1:
        return (n*(n+1)//2) % mod
    elif k == 2:
        return (n*(n+1)*(2*n+1)//6) % mod
    elif k == 3:
        return (n*n*(n+1)*(n+1)//4) % mod
    return -1

primes = []
composite = [0]*(Y+1)
N0sieve = [0]*(Y+1)
N0sieve[1] = 1

for i in range(2, Y):
    if not composite[i]:
        primes.append(i)
        N0sieve[i] = (i-1) % mod
    j = 0
    while j < len(primes) and i*primes[j] < Y:
        composite[i*primes[j]] = 1
        if i % primes[j] == 0: 
            N0sieve[i*primes[j]] = (N0sieve[i] * primes[j]) % mod
        else:
            N0sieve[i*primes[j]] = (N0sieve[i] * (primes[j] - 1)) % mod
        j += 1

N1sieve = [(N0sieve[i]*i) % mod for i in range(len(N0sieve))]
N2sieve = [(N0sieve[i]*i*i) % mod for i in range(len(N0sieve))]

for i in range(2, len(N0sieve)):
    N0sieve[i] = (N0sieve[i] + N0sieve[i-1]) % mod
    N1sieve[i] = (N1sieve[i] + N1sieve[i-1]) % mod
    N2sieve[i] = (N2sieve[i] + N2sieve[i-1]) % mod

N0key = {}
N1key = {}
N2key = {}

for v in FIinc(N+1):
    if v < Y:
        N0key[v] = N0sieve[v]
        N1key[v] = N1sieve[v]
        N2key[v] = N2sieve[v]
    else:
        x0 = sumpow(v, 1)
        x1 = sumpow(v, 2)
        x2 = sumpow(v, 3)
        for i in range(1, isqrt(v) + 1):
            x0 = (x0 - (N0sieve[i] - N0sieve[i-1]) * sumpow(v//i, 0)) % mod
            x1 = (x1 - (N1sieve[i] - N1sieve[i-1]) * sumpow(v//i, 1)) % mod
            x2 = (x2 - (N2sieve[i] - N2sieve[i-1]) * sumpow(v//i, 2)) % mod
            if i != 1:
                x0 = (x0 - N0key[v//i]*pow(i, 0)) % mod
                x1 = (x1 - N1key[v//i]*pow(i, 1)) % mod
                x2 = (x2 - N2key[v//i]*pow(i, 2)) % mod
        x0 = (x0 + N0key[isqrt(v)]*sumpow(isqrt(v), 0)) % mod
        x1 = (x1 + N1key[isqrt(v)]*sumpow(isqrt(v), 1)) % mod
        x2 = (x2 + N2key[isqrt(v)]*sumpow(isqrt(v), 2)) % mod
        N0key[v] = x0
        N1key[v] = x1
        N2key[v] = x2

N0key[0], N1key[0], N2key[0] = 0,0,0

del N0sieve, N1sieve, N2sieve, primes, composite

def F0(n, m):
    if n == 0: return 0
    return (2*N0key[n]-1) % m
def F1(n, m):
    if n == 0: return 0
    return (3*N1key[n]-1) % m
def F2(n, m):
    if n == 0: return 0
    return (N2key[n]) % m

def mm(k, m):
    return (((pow(2, k, m) - k*(k-1)//2 - k - 1)%m)+m)%m

def f(n, k, m):
    if n<=k: return 0
    x = (4*n*(n-k) + 4*n*n*F0(n//k, m) - 4*k*n*F1(n//k, m) + 4*k*k*F2(n//k, m)) % m
    return x

def sum2tok(n, m):
    return (pow(2, n, m) - n - 1 + m) % m

def sumk2tok(n, m):
    return (n-pow(2, n+1, m)+2)*(1-n)//2

def sumkk2tok(n, m):
    return (((pow(2, n, m)*((n-2)*n + 3) - n*(n+1)*(2*n+1)//6 - 3)%m) + m)%m

def weirdextrasum(n, m):
    return ((2*n*(-n*n - 3*n + pow(2, n+1, m) + 2))%m)


def T(n, m):
    rv = pow(2, (n+1)*(n+1), m) - (n+1)*(n+1) - 1
    x = 0
    #subtract the sum(4k*(n-k)*(2^(k-1)-1))
    x += weirdextrasum(n+1, m)

    x -= (f(n+1,3,m)*mm(2,m) + f(n+1,n+1,m)*mm(n+2,m)) % m
    x += (f(n+1,2,m)*mm(3,m) + f(n+1,n+2,m)*mm(n+1,m)) % m

    for k in range(3, isqrt(n+1) + 1):
        x += 4*(n+1)*(n+1)*F0((n+1)//k, m)*(pow(2, k-1, m) - 1)
        x -= 4*(n+1)*F1((n+1)//k, m)*(k*(pow(2, k-1, m) - 1))
        x += 4*F2((n+1)//k, m)*(k*k*(pow(2, k-1, m) - 1))
        x %= m
    for z in range(1, isqrt(n+1) + 1):
        k = (n+1)//z
        if (n+1)//z == z: continue
        fixedfor = (n+1)//z - (n+1)//(z+1)
        x += 4*(n+1)*(n+1)*F0((n+1)//k, m)*(sum2tok(k, m) - sum2tok(k-fixedfor, m))
        x -= 4*(n+1)*F1((n+1)//k, m)*(sumk2tok(k, m) - sumk2tok(k-fixedfor, m))
        x += 4*F2((n+1)//k, m)*(sumkk2tok(k, m) - sumkk2tok(k-fixedfor, m))
        x %= m
    return ((rv - x//2)%m + m) % m




print(T(N,mod) % 10**8)
print(time.time() - start)