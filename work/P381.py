def sieve(n):
    ps = [1]*(n+1)
    for i in range(2, n+1):
        if ps[i]:
            for i in range(i+i,n+1,i):
                ps[i] = 0
    return ps

def solve(n):
    primes = sieve(n)
    rv = 0
    brv = 4
    for i in range(7, n+1):
        t = i-1
        if primes[i]:
            rv = t
            for k in range(i-1, i-5, -1):
                t *= pow(k, -1, i)
                rv += t
            brv += rv % i
    return brv

print(solve(10**8))