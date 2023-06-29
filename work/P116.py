size = 50
solves = [0]*10000
cap = 3
def recbuild(lenleft, cap):
    if lenleft < cap: 
        return 1
    if lenleft == cap:  
        return 2
    if solves[lenleft] != 0: return solves[lenleft]
    else:   
        rv = 1
        for k in range(lenleft-cap+1):
            rv += recbuild(lenleft-cap-k, cap)
        solves[lenleft] = rv
        return rv
total = 0
total+=recbuild(size,2)
print(recbuild(size,2))
solves = [0]*10000
total+=recbuild(size,3)
print(recbuild(size,3))
solves = [0]*10000
total+=recbuild(size,4)
print(recbuild(size,4))
#-3 cause each have empty case
print(total-3)