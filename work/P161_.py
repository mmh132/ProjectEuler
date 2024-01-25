from functools import cache
from time import time

L, D = 9, 12
check = 2**L - 1
st = time()

@cache
def rec(r1, r2, r3, d):
    if d == 0:
        return 1 if r1+r2+r3 == 0 else 0
    if r1 == check:
        return rec(r2, r3, 0, d-1)
    
    s = 0
    while (r1 >> s)&1 == 1:
        s += 1
    rv = 0
    
    #line vertical
    if (r2 >> s)&1 == 0 and (r3 >> s)&1 == 0:
        rv += rec(r1 + (1 << s), r2 + (1 << s), r3 + (1 << s), d)
 
    
    #line horizontal
    if (r1 >> (s+1))&3 == 0 and s+2 < L:
        rv += rec(r1 + (7 << s), r2, r3, d) 
    
    # 1 1
    # 1 0
    if (r1 >> (s+1))&1 == 0 and (r2 >> s)&1 == 0 and s+1 < L:
        rv += rec(r1 + (3 << s), r2 + (1 << s), r3, d)
    
    # 1 1
    # 0 1
    if (r1 >> (s+1))&1 == 0 and (r2 >> (s+1))&1 == 0 and s+1 < L:
        rv += rec(r1 + (3 << s), r2 + (1 << (s+1)), r3, d)
    
    # 1 0
    # 1 1
    if (r2 >> s)&3 == 0 and s+1 < L:
        rv += rec(r1 + (1 << s), r2 + (3 << s), r3, d)
    
    # 0 1
    # 1 1
    if s != 0 and (r2 >> (s-1))&3 == 0:
        rv += rec(r1 + (1 << s), r2 + (3 << (s-1)), r3, d)
    
    return rv

print(rec(0,0,0,D))
print(time() - st)
