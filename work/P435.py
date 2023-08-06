import math
# def F(n, x):
#     if n == 0: return 0
#     if n == 1: return x
#     return x + x*F(n-1, x) + x*x*F(n-2,x)
# print(F(7,11))

#found nice recurrence, f_n = x + xf_n-1 + x^2f_n-2
#rewrote to length 3 to remove constant

def F2(n,x):
    if n == 0: return 0
    if n == 1: return x
    if n == 2: return x*x+x
    return F2(n-1,x)*(x+1) + F2(n-2,x)*(x*x-x) + F2(n-3,x)*(-x*x)

def matmul(m1, m2, mod):
    rv = [[0,0,0],[0,0,0],[0,0,0]]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                rv[a][b] += m1[a][c]*m2[c][b]%mod
            rv[a][b]%=mod
    return rv

def matrixBinaryPower(base, exp, mod):
    rv = [[1,0,0],[0,1,0],[0,0,1]]

    while exp:
        if exp&1:
            rv = matmul(rv, base, mod)
        base = matmul(base,base, mod)
        exp >>= 1
    
    return rv

def matvecprod(m, v):
    out = [0,0,0]
    for a in range(3):
        for b in range(3):
            out[a] += m[a][b]*v[b] 
    return out

def F(n, x, mod):
    base = [[x+1, x*x-x, -x*x],[1,0,0],[0,1,0]]
    rv = matrixBinaryPower(base, n, mod)
    return matvecprod(rv, [x*x+x,x,0])[2] % mod

print(matvecprod([[1,0,-2],[0,3,-1],[1,2,1]], [3,-1,4]))

mod = math.factorial(15)
print(sum(F(10**15, x, mod) for x in range(101))%mod)