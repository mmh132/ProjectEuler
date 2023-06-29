import sys
sys.setrecursionlimit(1000000000)
import time
start_time = time.time()
memo = dict()
def recbuildsplits(b,w, pilsize, step):
    if b == w == 0: return 1
    if pilsize > b+w: return 0
    if b<0 or w<0: return 0
    #if str(b) + str(w) + str(pilsize) + str(step) in memo: return memo[str(b) + str(w) + str(pilsize) + str(step)]
    remember = (b,w,pilsize,step)
    btake = pilsize-step
    wtake = step
    rv = 0
    if pilsize == step:
        while b >= 0 and w >= 0:
            rv += recbuildsplits(b,w,pilsize+1,0)
            b-=btake
            w-=wtake
    else:
        while b >= 0 and w >= 0:
            rv += recbuildsplits(b,w,pilsize,step+1)
            b-=btake
            w-=wtake
    memo[remember] = rv
    return rv
print(recbuildsplits(20,10,1,0))
print("--- %s seconds ---" % (time.time() - start_time))
    

