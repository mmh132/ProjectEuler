from math import log2

n = 100

def bin(n, k):
    if k == 0 or k == n: return 1
    rv = 1
    for i in range(n-k+1, n+1):
        rv *= i
    for i in range(2, k+1):
        rv //= i
    return rv

d = [1, 0]
for i in range(2,n+1):
    d.append((i-1)*(d[-1] + d[-2]))

def magicsum(n,z,k):
    x = 0
    for i in range(n-z+1):
        x += bin(n-z, i)*d[n-z-i]
    x *= bin(z,k)
    for i in range(z):
        x/=(n-i)
    return x

print(magicsum(100,25,22))    


