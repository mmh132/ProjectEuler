MOD = 10**9 + 7
def geometricseries(a1, r, n, m):
    return (a1*(pow(r, n, m) - 1)*pow(r-1, -1, m)) % m

def f(n):
    rv = 0
    for k in range(1, n+1):
        base = -k*k + 1
        base %= MOD
        rv += geometricseries(base,base,n,MOD)
        rv %= MOD
    return rv

print(f(10**6))
