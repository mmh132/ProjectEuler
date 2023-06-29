from math import sqrt
def ispfsq(n):
    a = sqrt(n)
    a = int(a)
    return a**2 == n
def solve(n):
    fac = [1]*(n+1)
    for i in range(2,n+1):
        for k in range(i, n+1, i):
            fac[k] += i**2
    rv = 0
    for idx, i in enumerate(fac):
        if ispfsq(i):
            rv += idx
    return rv
print(solve((64)*10**6))
