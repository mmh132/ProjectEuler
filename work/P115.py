size = 50
solves = [0]*10000
cap = 3
def recbuild(lenleft, cap):
    if lenleft < -1: return 0
    if lenleft < cap: return 1
    if lenleft == cap: return 2
    if solves[lenleft] != 0: return solves[lenleft]
    else:   
        rv = 1
        for i in range(cap,lenleft+1):
            for k in range(lenleft-i+1):
                rv += recbuild(lenleft-i-k-1, cap)
        solves[lenleft] = rv
        return rv
d = 0
n = 50
while d<1000000:
    d = recbuild(n,50)
    solves = [0]*(n+50)
    n+=1
print(n-1)