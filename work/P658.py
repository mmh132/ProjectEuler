from math import comb

def sum(a, n):
    rv = 0
    for i in range(n + 1):
        rv += a**i
    return rv

def I(k, n):
    rv = sum(k, n)
    for i in range(k+1):
        rv -= (-1) ** (k-i) * comb(k, i) * sum(i, n)
    return rv

print(I(3, 4))