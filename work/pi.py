
primes = []
def sieve(n):
    p = [1] * (n+1)
    for i in range(2, n+1):
        if not p[i]: continue
        for k in range(i+i, n+1, i):
            p[k] = False
    
    for i in range(2, n+1):
        if p[i]:
            primes.append(i)
    
    return 

