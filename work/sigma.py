from math import isqrt
def s(n):
    lsieve = [1]*(isqrt(n)+1)
    for i in range(2, n+1):
        for k in range(i, n+1, i):
            lsieve[k] += i
    S = dict()
    for z in range(isqrt(n), 0, -1):
        v = n//z
        
