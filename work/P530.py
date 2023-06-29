from math import gcd
def bfF(n):
    rv = 0
    for i in range(1, n+1):
        for j in range(1, n//i+1):
            rv += gcd(i,j)
    return rv

print(bfF(1000))