from copy import deepcopy as dc

zeroes = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def matmult(m1, m2, mod):
    newmat = dc(zeroes)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                newmat[i][j] += m1[i][k]*m2[k][j]
            newmat[i][j] %= mod
    return newmat

def matpow(base, exp, mod):
    rv = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    while exp:
        if exp&1:
            rv = matmult(rv, base, mod)
        base = matmult(base, base, mod)
        exp>>=1
    return rv

def vecprod(mat, vec):
    rvec = [0,0,0,0]
    for i in range(4):
        for j in range(4):
            rvec[i] += mat[i][j]*vec[j]
    return rvec

def doit(n, mod):
    n -= 4
    recmat = [[2,2,-2,1], [1,0,0,0], [0,1,0,0], [0,0,1,0]]
    newmat = matpow(recmat, n, mod)
    solution = vecprod(newmat, [8,4,1,1])
    print(solution[0]%10**8)

doit(10**12, 10**8)

    