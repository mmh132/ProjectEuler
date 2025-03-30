from math import gcd
def g(n):
    rv = 0
    for i in range(1, n+1):
        rv += pow(-1, i)*gcd(i*i, n)
    return rv

for i in range(1, 100):
    print(i, g(i))