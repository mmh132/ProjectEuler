from math import sqrt
cache = dict()
def totientsum(n):
    if n in cache: return cache[n]
    rv = n*(n+1) >> 1
    for g in range(2, int(sqrt(n)) + 1):
        rv -= totientsum(n//g)
    for z in range(1, int(sqrt(n)) + 1):
        if n//z != z:
            rv -= (n//z - n//(z+1))*totientsum(z)
    cache[n] = rv
    return rv

