from math import gcd

def radsieve(n):
    emp = list()
    s = []
    for i in range(n+1): s.append(emp.copy())
    for i in range(2, n+1):
        if s[i] == []:
            for k in range(i,n+1,i):
                s[k].append(i)
    return s

def p(l):
    rv = 1
    for i in l: rv*=i
    return rv

def hits(sub):
    rads = radsieve(sub)
    valid = []
    uCs = set()
    s = 0
    for i in range(len(rads)):
        if rads[i] == [i] or p(rads[i])<i:
            valid.append(i)

    for a1 in range(len(valid)):
        for b1 in range(a1+1, len(valid)):
            a,b = valid[a1], valid[b1]
            if a+b>sub: break
            if a+b not in valid: continue
            if gcd(a,b) != 1: continue
            if gcd(a, a+b) != 1: continue
            if gcd(b, a+b) != 1: continue
            if p(rads[a] + rads[b] + rads[a+b]) < a+b:
                uCs.add(a+b)
                s += a + b
                print(a, b, a+b)
    
    return s


print(hits(1000))

