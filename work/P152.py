from math import gcd
def add(a,b):
    n = a[0]*b[1]+b[0]*a[1]
    d = b[1]*a[1]
    g = gcd(n,d)
    return (n//g, d//g)
def sumbig(l):
    if len(l) == 2: 
        return add(l[0], l[1])
    else: 
        a = l.pop(0)
        b = l.pop(1)
        return sumbig([add(a,b)] + l)
def compare(a, b):
    return a[0]*b[1] < b[0]*a[1]


inp = 45
fracs = [(1, x**2) for x in range(2,inp + 1)]
found = {(0,1): 1}
temp = dict()
for n, f in enumerate(fracs):
    print(f,n)
    temp = found.copy()
    for i in found:
        a = add(i,f) 
        if a in temp: temp[a] += found[i]
        else: temp[a] = found[i]
    tocompare = sumbig(fracs[(n+1):])
    found = temp.copy()
    keydels = []
    for i in found:
        if compare(add(tocompare, i), (1,2)): keydels.append(i)
    for i in keydels:
        del found[i]
print(found[(1,2)])

