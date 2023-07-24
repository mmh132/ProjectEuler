from math import isqrt
def sieve(n):
    p = [1]*(n+1)
    for i in range(2, n+1):
        if not p[i]: continue
        for k in range(i+i, n+1, i):
            p[k] = 0
    return p

psieve = sieve(100)
def check(n):
    err = 0 if isqrt(n)**2 == n else 1
    for i in range(isqrt(n) + err, n+1):
        if n%i == 0 and psieve[i]:
            return False
    return True
t = 1
for i in range(2, 101):
    if check(i):
        print(i)
        t += 1
print(str(t) + " total")