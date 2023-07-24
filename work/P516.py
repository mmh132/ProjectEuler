from PrimeUtil import MillerRabin64 as mr

N = 10**12
smooth = list()
all = [2,3,5]
def dfs(n,i):
    if i == 3: 
        smooth.append(n)
        return
    while n <= N:
        dfs(n, i+1)
        n*=all[i]
dfs(1,0)
smooth.sort()
ps = []
for i in smooth:
    if mr(i+1) and i > 5:
        ps.append(i+1)
all = []
def dfs2(n,i):
    if n > N:
        return
    if i == len(ps):
        all.append(n)
        return
    dfs2(n, i+1)
    dfs2(n*ps[i], i+1)
    return
dfs2(1,0)
t = 0
for i in all:
    for k in smooth:
        if i*k <= N:
            t += i*k
        else:
            break
print(t)

