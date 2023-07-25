from math import isqrt

def tri(n):
    return n*(n+1)//2

def lsieve(n):
    tot = list(range(n+1))
    for i in range(2, n+1):
        if tot[i] != i:
            continue
        for k in range(i, n+1, i):
            tot[k] //= i
            tot[k] *= (i-1)
    for i in range(2, n+1):
        tot[i] += tot[i-1]
    return tot

def sumgcd(n, mod):
    y = int(n**(2/3))
    tots = lsieve(y)
    T = dict()
    #compute summatory totient from backtracking
    for v in range(1, isqrt(n) + 1):
        T[v] = tots[v]
    for z in range(isqrt(n), 0, -1):
        v = n//z
        if v <= y:
            T[v] = tots[v]
            continue
        x = tri(v)
        for i in range(1, isqrt(v) + 1):
            x -= (tots[i] - tots[i-1])*(v//i)
            if i!= 1:
                x -= T[v//i]
        x += T[isqrt(v)]*isqrt(v)
        T[v] = x
    print("here")
    #apply sqrt for final sum
    s = 0
    for v in range(1, isqrt(n) + 1):
        s += v * T[n//v]
        if n//v != v:
            s += (tri(n//v)-tri(n//(v+1)))*T[v]
        s %= mod
    return s
    
print(sumgcd(10**10, 998244353))
