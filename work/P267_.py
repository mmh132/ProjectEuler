def ternary(f, l, h, err):
    while f-l > err:
        m1, m2 = l + (h-1)/3, h - (h-1)/3
        f1, f2 = f(m1), f(m2)
        if f1 < f2: l = m1
        else: h = m2
    return f(l)

def pb(f):
    