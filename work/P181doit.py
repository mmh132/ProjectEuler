import sys
sys.setrecursionlimit(10000000)
import time
start_time = time.time()
memo = dict()
def recbuildsplits(b,w,size,sv):
    if (b,w,size,sv) in memo: return memo[(b,w,size,sv)]
    if b<0 or w<0: return 0
    if size == 1 or b+w == 0: return 1
    rv = recbuildsplits(b,w,size-1,0)
    wt,bt = 0,0
    for i in range(sv,size+1):
        wt = size-i
        bt = i
        rv += recbuildsplits(b-bt, w-wt, size,i)
    memo[(b,w,size,sv)] = rv
    return rv
b = 10
w = 20
print(recbuildsplits(b,w,b+w,0))
print("--- %s seconds ---" % (time.time() - start_time))
