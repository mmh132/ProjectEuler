from math import gcd
def bf(n):
    s = 0
    for k in range(1, n+1):
        for i in range(1, k+1):
            s += i//gcd(i,k)
    return s

def bfnew(n):
    s = n
    for i in range(1, n+1):
        for j in range(1, i):
            s += j//gcd(i,j)
    return s
print(bf(100))
print(bfnew(100))