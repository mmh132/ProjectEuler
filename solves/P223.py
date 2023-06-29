from math import sqrt
from P223tester import test
def fsieve(n):
    l = []
    rv = []
    for i in range(n+1):rv.append(l.copy())
    for i in range(1,len(rv)):
        for k in range(i, len(rv), i):
            rv[k].append(i)
    for i in range(len(rv)):
        newl = []
        while len(rv[i]) > 1:
            newl.append((rv[i].pop(0), rv[i].pop(-1)))
        if len(rv[i]) == 1: newl.append((rv[i][0], rv[i][0]))
        rv[i] = newl.copy()
    return rv
def lcomb(pset1, pset2):
    allsets = [(pset1[0][1], pset2[0][1])]
    for a in pset1: 
        for b in pset2:
            allsets.append((a[0]*b[0], a[1]*b[1]))
            allsets.append(tuple(sorted([a[0]*b[1], a[1]*b[0]])))
    return list(set(allsets))
inp = 25*10**6
print (inp//2)
lsieve = fsieve(inp//2)
t = 0
cs = set()
for b in range(2,len(lsieve)-1):
    if b %10**4 == 0: print (round(b/len(lsieve), 2)*100)
    for pair in lcomb(lsieve[b-1], lsieve[b+1]):
        if (pair[0] + pair[1]) % 2 == 0:
            if (pair[0] + pair[1])//2 + (pair[1] - pair[0])//2 + b <= inp and (pair[1] - pair[0])//2 <= b:
                cs.add(((pair[1] - pair[0])//2 , b, (pair[0] + pair[1])//2 ))
                t += 1
print(t)