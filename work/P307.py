from math import log10
f = [0] + [log10(i) for i in range(1, 1000001)]
for i in range(1, len(f)): f[i] += f[i-1]

def comb(n, a, b, c):
    return f[n] - f[a] - f[b] - f[c]

def p(k, n):
    x = 0
    for c in range(k//2 + 1):
        b = k-2*c
        a = n-b-c
        x += f[k]*comb(n,a,b,c)
    x -= k*log10(n)
    return 1-pow(10, x)

print(p(3, 7))
