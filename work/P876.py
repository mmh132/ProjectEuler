from copy import deepcopy as dc
def mm(a, b):
    rv = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                rv[i][j] += a[i][k]*b[k][j]
    return rv

def matvec(a, x):
    rv = [0,0,0]
    for i in range(3):
        for j in range(3):
            rv[i] += a[i][j]*x[j]
    return rv

x = [[1,0,0], [0,1,0], [0,0,1]]
y = [[1,2,3], [4,5,6], [7,8,9]]

f1 = [[-1,2,2], [0,1,0], [0,0,1]]
f2 = [[1,0,0], [2,-1,2], [0,0,1]]
f3 = [[1,0,0], [0,1,0], [2,2,-1]]

f12 = mm(f1, f2)
f21 = mm(f2, f1)
f13 = mm(f1, f3)
f31 = mm(f3, f1)
f23 = mm(f2, f3)
f32 = mm(f3, f2)

print(f12)
print(f21)
print(f13)
print(f31)
print(f23)
print(f32)

print(mm(f31, f23))