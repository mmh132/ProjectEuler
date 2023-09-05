from copy import deepcopy as dcop
mat = [
    [0,7,0,0,0,0,0],
    [0,1,6,0,0,0,0],
    [0,1,1,5,0,0,0],
    [0,1,1,1,4,0,0],
    [0,1,1,1,1,3,0],
    [0,1,1,1,1,1,2],
    [0,1,1,1,1,1,1]
]

zeroes = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

def matmul(ma,mb,mod):
    rm = dcop(zeroes)
    for i in range(7):
        for j in range(7):
            for k in range(7):
                rm[i][j] += ma[i][k]*mb[k][j]
                rm[i][j] %= mod
    return rm

def matpow(m, p, mod):
    out = dcop(zeroes)
    for i in range(7): out[i][i] = 1

    while p:
        if p&1:
            out = matmul(out,m,mod)
        m = matmul(m,m,mod)
        p>>=1
    
    return out

x = matpow(mat, 10**12 + 1, 10**9)
print(x)
print(x[0][1])