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

def sumtot(n, mod):
    y = int(0.25*n**(2/3))
    tots = lsieve(y)
    print("here")
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
    return T[n]%mod
x = int(input())
print(sumtot(x, 998244353))
