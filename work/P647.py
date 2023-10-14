from math import isqrt
def istri(n):
    if isqrt(2*n)*(isqrt(2*n) + 1) == 2*n: return True
    return False
def test(a,b):
    for i in range(1000):
        if not istri(a*i*(i+1)//2 + b): return False
    return True
s = 0
for a in range(1, 100):
    for b in range(1, 100):
        if test(a,b):
            print(a,b)
            s += a+b
print(s)
            
    