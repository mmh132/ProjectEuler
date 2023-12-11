from functools import cache as ccc
from math import sqrt
@ccc 
def fib(n):
    return 1 if n == 0 or n == 1 else fib(n-1) + fib(n-2)
p = 0
for k in range(1, 1000):
    p += fib(2*k-2)/(2**(2*k))
print(p)


def P(n):
    phi = (1+sqrt(5))/2
    rv = pow(1/phi, 2-n)/(pow(2,n) - pow(phi, n)) - pow(-phi, 2-n)/(pow(2,n) - pow(-phi, -n))
    return rv/sqrt(5)
