from math import isqrt

N, K, mod = 10**6, 999983, 10**9 + 7

def seg_sieve(n):
    n = int(n)
    S = 10**5

    primes = []
    nsqrt = isqrt(n)
    is_prime = [1] * (nsqrt+2)
    for i in range(2,nsqrt+1):
        if is_prime[i]:
            primes += [i]
            for j in range(i*i,nsqrt+1,i):
                is_prime[j] = 0

    result = []
    block = [0] * S
    for k in range(n//S+1):
        block[:] = [1]*S
        start = k * S
        for p in primes:
            start_idx = (start + p - 1) // p
            j = max(start_idx, p) * p - start
            while j < S:
                block[j] = 0
                j += p
        
        if k == 0:
            block[0] = block[1] = 0
        for i in range(S):
            if start + i > n:
                break
            if block[i]:
                result += [start+i]

    return result

def orconvolve(a, b):
    n = 0
    while (1 << n) < max(len(a), len(b)): 
        n += 1
    while len(a) < 1 << n:
        a.append(0)
    while len(b) < 1 << n:
        b.append(0)


    for i in range(n):
        for j in range(1<<n):
            if (j >> i) & 1:
                a[j] += a[j - (1 << i)]
                a[j] %= mod
                b[j] += b[j - (1 << i)]
                b[j] %= mod

    c = [(a[i]*b[i] % mod) for i in range(1 << n)]
    for i in range(n-1, -1, -1):
        for j in range((1 << n) - 1, -1, -1):
            if (j >> i) & 1:
                c[j] -= c[j - (1 << i)]
                c[j] %= mod
    
    for i in range(len(c)):
        c[i] += mod
        c[i] %= mod
    
    return c

def T(n, k):
    primes = set(seg_sieve(n))
    coeff = [0]*(n+1)
    for i in primes:
        coeff[i] += 1
    
    out = [1]
    #binary exponentiation
    while k:
        if k % 2 == 1:
            nout = orconvolve(out.copy(), coeff.copy())
            out = nout.copy()
        ncoeff = orconvolve(coeff.copy(), coeff.copy())
        coeff = ncoeff.copy()
        k >>= 1
    
    rv = 0
    for i in primes:
        rv = (rv + out[i]) % mod
    return rv 

print(T(N, K))
