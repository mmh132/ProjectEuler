from functools import cache
import sys
N = 100
coeff = [1/36,2/9,1/2,2/9,1/36]

@cache
def dp(p, t):
    #print(p,t)
    if t == 0:
        return 1 if p == N//2 else 0
    rv = 0
    cc = 0
    for i in range(p-2, p+3):
        x = min(abs(i), abs(i-N))
        if x == 0: continue
        rv += coeff[cc]*dp(x, t-1)
        cc+=1
    return rv
z = 0
for i in range(1000):
    print(dp(0, i)) 
    z += dp(0, i)
print(z)
#print(sum([dp(0, i)*i for i in range(1, 10000)]))