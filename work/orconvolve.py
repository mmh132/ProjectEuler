mod = 69
#a or convolve b in nlogn, FWHT algorithm
def orconvolve(a, b):
    n = 0
    while (1 << n) < max(len(a), len(b)): 
        n += 1
    while len(a) < 1 << n:
        a.append(0)
    while len(b) < 1 << n:
        b.append(0)


    for i in range(n):
        for j in range(1<<n):
            if (j >> i) & 1:
                a[j] += a[j - (1 << i)]
                a[j] %= mod
                b[j] += b[j - (1 << i)]
                b[j] %= mod

    c = [(a[i]*b[i] % mod) for i in range(1 << n)]
    for i in range(n-1, -1, -1):
        for j in range((1 << n) - 1, -1, -1):
            if (j >> i) & 1:
                c[j] -= c[j - (1 << i)]
                c[j] %= mod
    
    for i in range(len(c)):
        c[i] += mod
        c[i] %= mod
    
    return c