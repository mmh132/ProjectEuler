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
<<<<<<< Updated upstream
    print(i, bfderivative(i), gcd(i, bfderivative(i)))

a = 2*2*2*2*2*2*3*3*3*7
print(a, bfderivative(a), gcd(a, bfderivative(a)))
#theory: gcd(k, k') is a multiplicative function with
#f(p^k) = p^k - (0 if p|k else 1)

x = 0
for i in range(10000+1):
    x += gcd(i, bfderivative(i))
print(x)
=======
    print(i, bfderivative(i), gcd(i, bfderivative(i)), i//gcd(i, bfderivative(i)))
>>>>>>> Stashed changes
