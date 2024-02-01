from math import isqrt
N = 10**4

p = [0, 0] + [1]*(isqrt(N) - 1)
w = [0]*(isqrt(N) + 1)
for i in range(2, isqrt(N) + 1):
    if p[i]:
        w[i] = 1
        for j in range(i + i, isqrt(N) + 1, i):
            p[j] = 0
            if w[j] > -1:
                w[j] += 1
        for j in range(i*i, isqrt(N) + 1, i*i):
            w[j] = -1
            
vals = [0]*(max(w) + 1)
for i in range(1, isqrt(N) + 1):
    for j in range(w[i] + 1):
        vals[j] += pow(-1, w[i]+j)*(N//i//i)
print(vals)