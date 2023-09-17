def pow(n, e, m):
    rv = 1
    while e:
        if e&1: 
            rv = rv*n % m
        n = n*n % m
    return rv

def isqrt(n):
    if n == 1: return 1
    a = n >> 1
    b = n
    while a<b:
        c = (a+n//a) >> 1
        a,b = c,a
    return b

def exteuclid(r0, r1):
    flip = False
    if r0 > r1 : r0, r1 = r1, r0; flip = True
    s0, s1, t0, t1 = 1,0,0,1
    while r1 != 0:
        s0, s1 = s1, s0 - (r0//r1)*s1
        t0, t1 = t1, t0 - (r0//r1)*t1
        r0, r1 = r1, r0%r1
    return (r0, t0, s0) if flip else (r0, s0, t0)

def modinv(n, m):
    n %= m
    e = exteuclid(n,m)
    assert e[0] == 1
    return exteuclid(n, m)[1] % m

def crt(cg):
    m = 1
    for i in cg:
        m *= i[1]
    rv = 0
    for i in cg:
        a = i[0]
        m1 = m//i[1]
        n1 = modinv(m1, i[1])
        rv = (rv + a * m1 % m * n1) % m
    return rv
