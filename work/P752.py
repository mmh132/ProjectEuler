def matmul(ma, mb):
    rm = [[0,0],[0,0]]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                rm[a][b] += ma[a][c]*mb[c][b]
    return rm

def binpow(m, e):
    rm = [[1,0],[0,1]]
    while e:
        if e&1: 
            rm = matmul(rm,m)
        m = matmul(m,m)
        e//=2
    return m

def prod(mat, vec):
    rvec = [0,0]
    for i in range(2):
        for j in range(2):
            rvec[i] += mat[i][j]*vec[j]
    return rvec

def eval(n):
    print(prod(binpow([[1,7],[1,1]], n), [1,1]))
eval(2)
print(matmul([[1,0],[0,1]],[[1,0],[0,1]]))
