size = 5
solves = [0]*58
sizes = [2,3,4]
def recbuild(lenleft):
    if lenleft < -1: return 0
    if lenleft < 2: return 1
    if lenleft == 2: return 2
    if solves[lenleft] != 0: return solves[lenleft]
    else:   
        rv = 1
        for i in range(len(sizes)):
            for k in range(lenleft-sizes[i]+1):
                rv += recbuild(lenleft-sizes[i]-k)
        solves[lenleft] = rv
        return rv
print(recbuild(50))
print(solves)
print(solves[50])
