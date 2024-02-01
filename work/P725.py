def ds(s, l):
    if l == 1:
        return s
    rv = 0
    for dig in range(10):
        rv += 10*ds(s-dig, l-1)
    return rv

def S(n):
    rv = 0
    for l in range(1, n+1):
        for d in range(1, n+1):
            rv += (ds(d, l) - ds(d, l-1))