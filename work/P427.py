def f(n, k):
    if k == n:
        return n
    rv = (n-k)*n*(n-1)*pow(n, n-k-1)
    rv += n*pow(n, n-k)
    return rv


print(f(3, 1) - f(3, 2))