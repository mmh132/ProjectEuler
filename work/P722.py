from math import log10
def pow(n, e):
    rv = 0
    while e:
        if e&1:
            rv = rv*n
        n=n*n
    return rv
        
LIM = 3000000
def f(k, q):
    x = 0
    for d in range(1, LIM):
        x += pow(d, k)*pow(q, d)*pow(1-pow(q,d), -1)
    return x

print(f(7, 1-2**(-15)))


