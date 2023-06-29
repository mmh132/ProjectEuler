from copy import deepcopy as dc
row = [0]*2000
zeroes = []
for i in range(2000):
    zeroes.append(row.copy())

def matmult(m1, m2, mod):
    newmat = dc(zeroes)
    for i in range(2000):
        for j in range(2000):
            for k in range(2000):
                newmat[i][j] += m1[i][k]*m2[k][j]
            newmat[i][j] %= mod
    return newmat

def matpow(base, exp, mod):
    rv = dc(zeroes)
    for i in range(2000):
        rv[i][i] = 1
    while exp:
        if exp&1:
            rv = matmult(rv, base, mod)
        base = matmult(base, base, mod)
        exp>>=1
        print(exp)
    return rv

def vecprod(mat, vec):
    rvec = [0]*2000
    for i in range(2000):
        for j in range(2000):
            rvec[i] += mat[i][j]*vec[j]
    return rvec

def doit(n, mod):
    n -= 2000
    recmat = dc(zeroes)
    recmat[0][1998] = 1
    recmat[0][1999] = 1
    
    for i in range(1999):
        recmat[i+1][i] = 1
    print(recmat[1999])
    newmat = matpow(recmat, n, mod)
    solution = vecprod(newmat, [1]*2000)
    print([i%mod for i in solution])

doit(10**18, 20092010)

    