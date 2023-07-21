from math import isqrt
cache = dict()
def distline(n):
    if n in cache: return cache[n]
    rv = (n+1)**3 - 1
    for g in range(2, isqrt(n) + 1):
        rv -= distline(n//g)
    for z in range(1, isqrt(n) + 1):
        if n//z != z:
            rv -= (n//z - n//(z+1))*distline(z)
    cache[n] = rv
    return rv

def solve(n):
    x = str(distline(n))
    out = ""
    for i in range(9):
        out += x[i]
    for i in range(9, 0, -1):
        out += x[-i]
    print(out)

print(solve(10**10))