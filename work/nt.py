from math import isqrt

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

def generalconvolve(f,g,F,G,n, mod = 0):
    rv = 0
    for i in range(1, isqrt(n) + 1):
        rv += f(i)*G(i)
        rv += g(i)*F(i)
        if mod: rv %= mod
    rv -= F(isqrt(n))*G(isqrt(n))
    if mod: rv += mod; rv %= mod
    return rv

stk = [(1,1,0)]
def powerfulnumbersext(n, h, mod):
    primes = seg_sieve(isqrt(n)+1)
    while stk:
        c = stk.pop(0)
        nn, hn, i= c[0], c[1], c[2]
        if i == len(primes): yield (nn, hn); continue
        p, e = primes[i], 2
        while nn*p**e < n:
            stk.append((nn*p**e, (hn*h(p,e)) % mod, i+1))
            e += 1

def linearsieve_mult(n, f):
    c, func, cnt = [1]*(n+1), [1]*(n+1), [1]*(n+1)
    primes = []
    for i in range(2, n):
        if not c[i]: primes.append(i)
        