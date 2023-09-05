from math import isqrt
def G(n):
    mob = [1]*(n+1)
    prime = [1]*(n+1)
    for i in range(2, n+1):
        if prime[i]:
            mob[i] *= -1
            for j in range(i+i, n+1, i):
                mob[j]*=-1
                prime[j] = 0
            for j in range(i**2, n+1, i**2):
                mob[j] = 0
    
    ww = [n]*(n+1)
    for i in range(n+1):
        ww[i]-=i
    for d in range(2, n+1):
        for k in range(d, n+1, d):
            ww[k] += mob[d]*(n//d - k//d)

    
    rv = 1
    for i in range(2, n+1):
        rv *= pow(i, ww[i], 10**9 + 7)
        rv %= 10**9 + 7
    return rv

print(G(10**8))
    