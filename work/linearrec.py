from math import gcd

def mul(a, b, m):
    c = [0]*(len(a) + len(b) - 1)
    for e_i, a_i in enumerate(a):
        for e_j, b_j in enumerate(b):
            c[e_i + e_j] = (c[e_i + e_j] + a_i*b_j) % m
    while c[-1] == 0: c.pop(-1)
    return [0] if c == [] else c

def add(a, b, m):
    if len(a) < len(b):
        return add(b, a, m)
    c = a.copy()
    for e_i, b_i in enumerate(b):
        c[e_i] = (c[e_i] + b_i) % m
    while c[-1] == 0: c.pop(-1)
    return [0] if c == [] else c

def div(n, d, m):
    q = []
    r = n
    while r != [] and len(r) >= len(d):
        t = [0]*(len(r) - len(d)) + [r[-1]*pow(d[-1], -1, m)]
        q = add(q, t, m)
        r = add([-i for i in r], mul(t, d, m), m)
    return (q, r)

print(mul([0,0,2], [1,2,3], 10**9+7))

x = div([-4, 0, -2, 1], [-3, 1], 10**9+7)
print(add(mul(x[0], [-3, 1], 10**9+7), x[1], 10**9+7))


