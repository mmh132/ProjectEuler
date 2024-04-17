uyfrom math import factorial
from functools import cache

N = 60
arr = [0] * (N + 1)

@cache
def dp(n_0, n_1, n_2, n_3, m):

    if n_0 + n_1 + n_2 + n_3 == 0:
        return tuple([0]*m + [1] + [0]*(N-m))
    rv = [0] * (N + 1)
    if n_0 > 0:
        x = dp(n_0-1, n_1+1, n_2, n_3, max(m, n_1+n_2+n_3))
        for i in range(N + 1):
            rv[i] += 4*n_0*x[i]
    if n_1 > 0:
        x = dp(n_0, n_1-1, n_2+1, n_3, max(m, n_1+n_2+n_3))
        for i in range(N + 1):
            rv[i] += 3*n_1*x[i]
    if n_2 > 0:
        x = dp(n_0, n_1, n_2-1, n_3+1, max(m, n_1+n_2+n_3))
        for i in range(N + 1):
            rv[i] += 2*n_2*x[i]
    if n_3 > 0:
        x = dp(n_0, n_1, n_2, n_3-1, max(m, n_1+n_2+n_3))
        for i in range(N + 1):
            rv[i] += n_3*x[i]
    return tuple(rv)

out = dp(N, 0, 0, 0, 0)
print(out)
rv = 0
for i in range(N + 1):
    rv += i * out[i]
print(rv / factorial(4*N))
