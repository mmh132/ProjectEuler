from math import factorial as fac
def perms(l,last,yet):
    if len(l) == 0 and yet == True: return 1
    if yet:
        for i in l:
            if i > last: return 0
        return 1
    rv = 0 
    tmp = l.copy()
    for i in range(len(l)):
        tmp = l.copy()
        tmp.pop(i)
        rv += perms(tmp, l[i], l[i]>last)
    return rv
def choose(n,k):
    return fac(n)//(fac(n-k)*fac(k))
def p(n):
    return choose(26,n)*perms(list(range(1,n+1)), n+1, False)
x = []
for i in range(2,26):
    x.append(p(i))
    print(max(x))