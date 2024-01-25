from math import isqrt, log

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

N = 500500
C = N

while C/log(C) < N:
    C += N
    
prime = seg_sieve(C)
while len(prime) > N:
    prime.pop(-1)
    
l, u = 0, N - 1
exp = [1]*N
doinggood = 0

while doinggood < 2:
    if prime[l]**(exp[l] + 1) < prime[u]:
        exp[u] = 0
        exp[l] += exp[l] + 1
        u -= 1
        doinggood = 0
    else:
        l += 1
        doinggood += 1
        
MOD = 500500507
rv = 1
for i in range(N):
    rv *= pow(prime[i], exp[i], MOD)
    rv %= MOD
print(rv)