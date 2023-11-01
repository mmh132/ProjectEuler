from math import log, exp
def p(k, n):
    f = [0,0]
    for i in range(2, n+1):
        f.append(f[-1] + log(i))

    rv = 0
    for p2 in range(k//2 + 1):
        thing = f[n] - f[n-k+p2] - f[p2] - f[k-2*p2] + f[k] - (p2)*log(2) - k*log(n)
        rv += exp(thing)
    return 1 - rv
print(p(3,7))
print(round(p(20000,10**7), 10))