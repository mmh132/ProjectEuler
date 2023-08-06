from math import e,sqrt

m = dict()
def comb(n, k):
    if k <= 0 or k >= n: return 1
    if (n,k) in m: return m[(n,k)]
    x = comb(n-1,k-1) + comb(n-1,k)
    m[(n,k)] = x
    return x

def val(n):
    rv = 0
    for j in range(n//2 + 1):
        if j&1:
            rv -= comb(n+1,j)*pow(n//2-j+1, n)
        else:
            rv += comb(n+1,j)*pow(n//2-j+1, n)
    return rv

def f(n):
    x = val(2*n - 1)
    print(x)
    for i in range(2, 2*n):
        x /= i
    print(round(x, 10))

f(80)
