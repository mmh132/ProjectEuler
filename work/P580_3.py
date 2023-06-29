memo = dict()

def primesieve(n):
    primes = [1]*(n+1)
    for i in range(2, n+1):
        if primes[i]:
            for k in range(i+i, n+1, i):
                primes[k] = 0
    return primes

def f(n):
    if n in memo: return memo[n]
    rv = n
    for k in range(3, int(n**0.5) + 1, 2):
        rv -= f(n//(k*k))
    memo[n] = rv
    return rv

inp = 10**7
t = (inp-1)//4 + 1
s = f(t)
primes = primesieve(int(inp**0.5))
for i in range(3, len(primes), 4):
    if primes[i]:
        s += f(t//(i*i))
print(s)