from math import log10
LIM = 3000000
def f(k, q):
    x = 0
    for n in range(1, LIM):
        x += pow(n, k)*pow(q, n)*pow(1-pow(q,n), -1)
    return x

print(f(7, 1-2**(-15)))