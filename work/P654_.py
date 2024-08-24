import numpy as np

N, M = 50, 10**12
MOD = 10**9 + 7

mat = np.zeros((N, N), dtype=np.int64)

for i in range(N):
    for j in range(N):
        mat[i, j] = 1 if i + j + 2 <= N else 0

mat = np.asarray(mat)

def matmult(m1, m2):
    newmat = np.asarray(np.zeros((N, N), dtype=int))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                newmat[i][j] += m1[i][k]*m2[k][j]
            newmat[i][j] %= MOD
    return newmat

def matpow(base, exp):
    rv = np.asarray(np.eye(N, dtype=int))
    while exp:
        print(exp)
        if exp & 1:
            rv = matmult(rv, base)
        base = matmult(base, base)
        exp >>= 1
    return rv

out = matpow(mat, M)

#print(out)
rv = int(np.sum(out[0, :]) % MOD)
print(rv)