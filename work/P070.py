def isper(n,n2):
    if len(str(n)) != len(str(n2)): return False
    if sorted(str(n)) != sorted(str(n2)): return False
    return True

def factorsieve(n):
    blank = []
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == []:
            rv[i].append(i)
            for k in range(i+i,len(rv),i):
                rv[k].append(i)
    return rv

def phi(val,n):
    tot = val
    div = 1
    for i in n:
        tot*=(i-1)
        div*=i
    return tot//div

inp = 10**7
things = factorsieve(inp)
best = 10000000000
abc = 1
print(phi(10,things[10]))
for i in range(2,len(things)):
    c = phi(i,things[i])
    if isper(c,i):
        if i/c<best: 
            best = i/c
            abc = i
print(abc)