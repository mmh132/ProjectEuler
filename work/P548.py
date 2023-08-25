from math import isqrt
def isprime(n):
    for i in range(2, isqrt(n) + 1):
        if n%i == 0:
            return False
    return True

def g(n):
    if n == 1 or isprime(n):
        return 1
    else:
        rv = 0
        for i in range(1, n):
            if n%i == 0:
                rv += g(i)
        return rv

print(g(12), g(48), g(120))
