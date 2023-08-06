from math import isqrt
def ctdv(n):
    t = -1 if isqrt(n)*isqrt(n) == n else 0
    for i in range(1, isqrt(n) + 1):
        if n%i == 0:
            t += 2
    return t

for k in range(1, 101):
    if ctdv(k) % 6 == 1:
        print(k)
    
