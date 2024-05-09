from math import gcd
from functools import cache

N = 1000
ss = [
    (0,0,1),
    (0,1,0),
    (1,0,0),
    (1,1,0),
    (1,0,1),
    (0,1,1),
    (1,1,1)
]

s = {(0,0,0): 0}

rv = 0
for i in range(N + 1):
    for j in range(i, N + 1):
        for k in range(j, N + 1):
            if (i, j, k) not in s: s[(i, j, k)] = 0
            if s[(i, j, k)] == 1: continue
            rv += i + j + k
            for mask in ss:
                for m in range(1, N + 1):
                    nv = tuple(sorted([i+m*mask[0], j+m*mask[1], k+m*mask[2]]))
                    if max(nv) > N: break
                    s[nv] = 1 

print(rv)