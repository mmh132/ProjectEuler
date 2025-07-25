from functools import cache

def g(n):
    if n == 1: return 1
    rv = 0  
    for i in range(1, n):
        if n%i == 0:
            rv += g(i)
    return rv

print(g(120))