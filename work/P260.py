from math import gcd
from functools import cache

N = 100
ss = [
    (0,0,1),
    (0,1,0),
    (1,0,0),
    (1,1,0),
    (1,0,1),
    (0,1,1),
    (1,1,1)
]

@cache
def dp(s):
    if s == (0,0,0): return False
    a, b, c = s
    for i in range(1, N + 1):
        for mask in ss:
            nv = [a - i*mask[0], b - i*mask[1], c - i*mask[2]]
            if nv[0] > -1 and nv[1] > -1 and nv[2] > -1:
                if not dp(tuple(sorted(nv))):
                    return True
    return False

print(dp((0,0,2)))

rv = 0
for i in range(N + 1):
    print(i)
    for j in range(i, N + 1):
        for k in range(j, N + 1):
            if not dp((i, j, k)):
                rv = rv + i + j + k
                assert i <= j <= k
print(rv)