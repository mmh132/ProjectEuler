def rng(n,m):
    x = 290797
    for i in range(n):
        yield x % m
        x = x*x % 50515093

def sp(n, e, m):
    rv = 0
    for i in range(min(e, 9) + 1):
        rv += pow(n,i,m)
        rv %= m
    return rv
def NF(p,q,m):
    rv, ct = 0,0
    for i in rng(q, p):
        rv += i*sp(p,ct-1, m)
        rv %= m
        ct += 1
    return rv

print(NF(61, 10**7, pow(61, 10)))
