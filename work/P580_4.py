
memo = dict()
def f(n, div):
    if (n, div) in memo: return memo[(n, div)]
    rv = (n-1)//div//4 + 1
    for i in range(3, int((n//(div))**0.5), 2):
        rv -= f(n, div*i*i)
    memo[(n, div)] = rv
    return rv



def primesieve(n):
    primes = [1]*(n+1)
    for i in range(2, n+1):
        if primes[i]:
            for k in range(i+i, n+1, i):
                primes[k] = 0
    return primes

inp = 10**7
s = f(inp, 1)
primes = primesieve(int(inp**0.5))
for i in range(3, len(primes), 4):
    if primes[i]:
        s += f(inp, i*i)
print(s)
    