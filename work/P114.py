size = 50
solves = [0]*(size+1)
def recbuild(lenleft):
    if lenleft < -1: return 0
    if lenleft < 3: return 1
    if lenleft == 3: return 2
    if solves[lenleft] != 0: return solves[lenleft]
    else:   
        rv = 1
        for i in range(3,lenleft+1):
            for k in range(lenleft-i+1):
                rv += recbuild(lenleft-i-k-1)
        solves[lenleft] = rv
        return rv
print(recbuild(size))
print(solves[size])
