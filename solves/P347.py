def factorsieve(n):
    blank = []
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == []:
            rv[i].append(i)
            for k in range(i+i,len(rv),i):
                rv[k].append(i)
    return rv
def S(n):
    facs = factorsieve(n)
    fset = set()
    rv = 0
    for i in range(1, n+1):
        if len(facs[-i]) == 2:
            if tuple(sorted(facs[-i])) not in fset:
                fset.add(tuple(sorted(facs[-i])))
                rv += n-i+1
    return rv
print(S(10**7))

