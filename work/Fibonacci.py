
def matrixMult(m1, m2, mod):
    rv = [[0,0],[0,0]]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                rv[a][b] += m1[a][c]*m2[c][b]%mod
            rv[a][b]%=mod
    return rv

def matrixBinaryPower(base, exp, mod):
    rv = [[1,0],[0,1]]

    while exp:
        if exp&1:
            rv = matrixMult(rv, base, mod)
        base = matrixMult(base,base, mod)
        exp >>= 1
    
    return rv

def fib(n, mod):
    base = [[1,1],[1,0]]
    rv = matrixBinaryPower(base, n, mod)
    return rv[0][1]


