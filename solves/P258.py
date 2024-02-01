def mul(a, b, mod):
    rv = [0]*(len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            rv[i+j] += a[i]*b[j]
            rv[i+j] %= mod
    return rv
