N, MOD = 24, 10**9
f = [0,1]
while len(f) < N+1:
    f.append(f[-1] + f[-2])
print(f)
    
p = [0,0] + [1]*(f[-1]+ 1)
for i in range(2, len(p)):
    if p[i]: 
        for j in range(i+i, len(p), i):
            p[j] = 0

def add(a, b, mod):
    rv = [0]*(max(len(a), len(b)))
    for i in range(max(len(a), len(b))):
        if i < len(a):
            rv[i] = (rv[i] + a[i]) % mod
        if i < len(b):
            rv[i] = (rv[i] + b[i]) % mod
    return rv

def karatsuba(a, b, n, mod):
    if len(a) == 1 and len(b) == 1:
        return [a[0]*b[0]]
    while len(a) > len(b): b.append(0)
    while len(b) > len(a): a.append(0)

    m = len(a)//2

    a1, a2 = a[0:m], a[m:n]
    b1, b2 = b[0:m], b[m:n]

    r1 = karatsuba(a1, b1, n, mod)
    r4 = karatsuba(a2, b2, n, mod)
    ap = add(a1, a2, mod)
    bp = add(b1, b2, mod)
    s = karatsuba(ap, bp, n, mod)
    t = add(s, [-x for x in add(r1, r4, mod)], mod)
    r = add(r1, add([0]*m + t, [0]*(2*m) + r4, mod), mod)
    while len(r) > n:
        r.pop(-1)
    return r

gf = [1]
for i in range(2, f[-1]):
    print(i)
    if p[i]:
        tomul = [1] + [0]*f[-1]
        c, e = i, i
        while e < len(tomul):
            tomul[e] = c
            e += i
            c = (c*i) % MOD
        gf = karatsuba(gf, tomul, f[-1] + 10, MOD)

tp = 0
for i in range(2, N+1):
    print(f[i])
    tp = (tp + gf[f[i]]) % MOD
print(tp)
