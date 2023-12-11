from math import gcd
n=10
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if gcd(i*i+1, j*j+1) != 1:
            print(i, j, gcd(i*i+1, j*j+1))