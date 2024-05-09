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

def E(n):
    primes = seg_sieve(n)
    