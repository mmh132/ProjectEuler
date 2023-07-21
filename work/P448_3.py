from math import isqrt

def lsieve(n):
    rv = list(range(n+1))
    for i in range(2, n+1):
        if rv[i] == i:
            rv[i] = i-1
            for k in range(i+i, n+1, i):
                rv[k] //= i
                rv[k] *= (i-1)
    for i in range(2, n+1):
        rv[i] *= i
    return rv

def N(x):
    return x*(x+1) >> 1

def N2(x): 
    return x*(x+1)*(2*x+1)//6

def fastinv(n):
    g = lsieve(isqrt(n))
    G = dict()
    G[1] = 1

    for v in range(2, isqrt(n) + 1):
        x = N2(v)
        for i in range(1, isqrt(v) + 1):
            x -= g[i]*N(v//i)
            if i != 1:
                x -= i*G[v//i]
        x += G[isqrt(v)]*N(isqrt(v))
        G[v] = x
    
    for z in range(isqrt(n), 0, -1):
        v = n//z
        x = N2(v)
        for i in range(1, isqrt(v) + 1):
            x -= g[i]*N(v//i)
            if i != 1:
                if v//i not in G: print(v//i-1 in g, v//i + 1 in g)
                x -= i*G[v//i]
        x += G[isqrt(v)]*N(isqrt(v))
        G[v] = x

    return G

def final(n):
    rv = n
    G = fastinv(n)
    g = lsieve(isqrt(n))
    for i in range(1, isqrt(n) + 1):
        rv += g[i]*(n//i)
        rv += G[n//i]
    rv -= G[isqrt(n)]*isqrt(n)
    return rv//2


x = final(999999)

print(x)
print(x % 999999017)
