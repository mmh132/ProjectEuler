def naivemul(a, b, mod = 0):
    rv = [0]*(len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            rv[i+j] += a[i]*b[j]
            if mod:
                rv[i+j] %= mod
    return rv

#coefficient c, starting values s, index k
def linearRec(c, s, k, mod = 0):
    def mul(a, b):
        rv = naivemul(a, b, mod)
        for i in range(len(rv) - 1, n-1, -1):
            for j in range(n-1, -1, -1):
                rv[i-j-1] += rv[i]*c[j]
                if mod: rv[i-j-1] %= mod
        return rv[:n]
    
    n = len(c)
    assert n <= len(s)

    a = [c[0]] if n == 1 else [0,1]
    x = [1]
    while k:
        if k&1: x = mul(x, a)
        a = mul(a, a)
        k//=2
    x = x[:n] + [0] * (n - len(x))

    rv = 0
    for i in range(n):
        rv += x[i]*s[i]
        if mod: rv %= mod
    return rv

print(linearRec([0]*1998 + [1,1], [1]*2000 , 10**18, 20092010))