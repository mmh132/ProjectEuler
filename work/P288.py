from math import factorial
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
#print(NF(3, 10**4, pow(3, 20)))
#print(NF(61, 10**7, pow(61, 10)))

def NF(p, q, mp):
    mod = pow(p, mp)
    digits = [290797]
    while len(digits) < q:
        digits.append(digits[-1]*digits[-1] % 50515093)
    digits = [i%p for i in digits]
    def dm():
        rv = 0
        for n, i in enumerate(digits):
            if n > mp: break
            rv += i*p**n
        return rv % mod
    def dd():
        digits.pop(0)
    rv = 0
    dd()
    while len(digits) > 0:
        if len(digits) % 100 == 0:
            print(len(digits)/q)
        rv += dm()
        dd()
        rv %= mod
    return rv 
print(NF(61, 10**7, 10))
    
            