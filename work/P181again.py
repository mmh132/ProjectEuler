import sys
sys.setrecursionlimit(10000000)
import time
start_time = time.time()
memo = dict()
def retsplit(b,w,bt,wt):
    #print(b,w,bt,wt)
    if b == w == 0: return 1 
    if bt == 1 and wt == 0: return 1
    if bt == 0 and wt == 1: return 1
    if (b,w,bt,wt) in memo: return memo[(b,w,bt,wt)]
    rv = 0
    if bt == -1 or wt>w:
        newsplit = bt + wt
        if newsplit<=b:
            rv += retsplit(b,w,newsplit-1,0)
        else:
            rv += retsplit(b,w,b,newsplit-1-b)
    if bt<=b and wt<=w:
        while b>=0 and w>=0:
            rv += retsplit(b,w,bt-1,wt+1)
            b-=bt
            w-=wt
    memo[(b,w,bt,wt)] = rv
    return rv
b,w = 1,3
print(retsplit(b,w,b,w))
print(retsplit(w,b,w,b))

print("--- %s seconds ---" % (time.time() - start_time))