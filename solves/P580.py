memo = dict()
def f(n):
    if n in memo: return memo[n]
    rv = (n-1)//4 + 1
    for k in range(3, int(n**0.5) + 1, 2):
        rv -= f(n//(k*k))
    memo[n] = rv
    return rv

def primesieve(n):
    primes = [1]*(n+1)
    for i in range(2, n+1):
        if primes[i]:
            for k in range(i+i, n+1, i):
                primes[k] = 0
    return primes

inp = 10**16
s = f(inp)
primes = primesieve(int(inp**0.5))
for i in range(3, len(primes), 4):
    if primes[i]:
        s += f(inp//(i*i))
print(s)
    
