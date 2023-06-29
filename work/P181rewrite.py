import sys
sys.setrecursionlimit(10000000)
import time
start_time = time.time()
memo = dict()
def retsplit(b,w,tot,inc):
    diff = (b-inc,tot-(b-inc))
    if diff[0] < 0 or diff[1]>w or inc>tot: return False
    return diff
def recbuildsplits(b,w,tot, inc):
    if b == w == 0:  return 1
    if tot == 1: return 1
    remember = (b,w,tot,inc)
    #print(remember)
    if remember in memo: return memo[remember] 
    rv = 0
    call = retsplit(b,w,tot,inc)
    if call == False:
        return recbuildsplits(b,w,tot-1,0)
    else:
        while b>=0 and w>=0:
            rv += recbuildsplits(b,w,tot,inc+1)
            b-=call[0]
            w-=call[1]
    memo[remember] = rv
    return rv



b = 1
w = 3
print(recbuildsplits(b,w,b+w,0))

print("--- %s seconds ---" % (time.time() - start_time))
    