from math import factorial as fac, comb

def f(d, r):
    if d < 0: return 0
    if d == 0: return fac(r)
    return (d-1)*f(d-2, r+1) + r*f(d-1, r)

x = comb(25, 22)*f(22, 75)
for i in range(2, 101):
    x/=i
print(round(x, 12))