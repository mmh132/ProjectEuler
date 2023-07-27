import sys
sys.setrecursionlimit(100000)
N = 10
LIM = 10000
m = dict()
def dp(p, d):
    p = min(p, N-p)
    if p == 0: return 0
    if d > LIM: return 0
    if p in m: return m[p]
    x = 0
    x += (1/36)*(1+dp(p-2, d+1))
    x += (2/9)*(1+dp(p-1, d+1))
    x += (1/2)*(1+dp(p, d+1))
    x += (2/9)*(1+dp(p+1, d+1))
    x += (1/36)*(1+dp(p+2, d+1))
    m[p] = x
    return x

print(dp(5, 0))