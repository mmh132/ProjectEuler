def g(n, k):
    if n==k: return n
    return (n-k)*pow(n, n-k+1)

def f(n, k):
    if n == k: return n
    return g(n, k) - g(n, k+1)

def F(n):
    rv = 0
    for i in range(1, n+1):
        rv += f(n, i)
        print(i, n, f(n, i))
    return rv

print(F(3))