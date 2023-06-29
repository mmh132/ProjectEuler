from math import factorial as f
numdie_cap_sides_topn = [20,70,12,10]
ways = []
def findthings(setnums):
    rv = 0
    ref = min(setnums)
    for i in range(len(allsets[ref])):
        rv += f(numdie_cap_sides_topn[0])//(finddivset(setnums + allsets[ref][i]))
    return rv
def finddivset(setnums):
    setnums = sorted(setnums)
    absnum = [1]
    ptr = 0
    for i in range(0, len(setnums)-1):
        if setnums[i] == setnums[i+1]:
            absnum[ptr] += 1
        else:
            ptr+=1
            absnum.append(1)
    div = 1
    for i in range(len(absnum)): div*=f(absnum[i])
    return div
def partink(n,k,cap,rv):
    rv = rv.copy()
    if n<0 or k<0: return
    if k == 0 and n == 0:
        ways.append(rv)
        return
    if cap>n: cap = n
    for i in range(cap,0,-1):
        partink(n-i,k-1,i,rv+[i])
partink(numdie_cap_sides_topn[1],numdie_cap_sides_topn[3],numdie_cap_sides_topn[2],[])
allsets = [[],[],[],[],[],[],[],[]]
def allsetssub(size,cap,rv,rcap):
    rv = rv.copy()
    if size<0: return
    if size == 0: allsets[rcap].append(rv); return
    for i in range(cap,0,-1):
        allsetssub(size-1,i,rv+[i],rcap)
for i in range(1,8): allsetssub(numdie_cap_sides_topn[0]-numdie_cap_sides_topn[3],i,[],i)
total = 0
for i in range(len(ways)): total+=findthings(ways[i])
print(int(total))


