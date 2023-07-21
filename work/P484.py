from Frac import fraction as fr
from math import gcd

def bfderivative(n):
    sieve = [1]*(n+1)
    for i in range(2, n+1):
        if sieve[i]:
            for k in range(i+i,n+1,i):
                sieve[k] = 0
    
    def vp(n, p):
        x = 0
        while n%p == 0:
            n//=p
            x += 1
        return x

    rv = fr(0,1)
    for i in range(2, n+1):
        if sieve[i]:
            rv += fr(vp(n, i), i)
    
    return (rv*fr(n, 1)).n

print(bfderivative(60))

for i in range(1, 100):
    print(i, bfderivative(i), gcd(i, bfderivative(i)))

a = bfderivative(32)
b = bfderivative(5)
print(bfderivative(5*2**5))