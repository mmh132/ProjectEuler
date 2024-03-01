from math import comb

def s(n):
    rv = 0
    for i in range(n + 1):
        rv += comb(n, i)*i**n
    return rv

print(s(10), s(4))