from math import sqrt
def F(x):
    return x*(x+1)*(2*x+1)//6
def G(x):
    return x
def f(x):
    return x*x
def g(x):
    return 1
def SIGMA2(x):
    A = int(sqrt(x))
    B = int(sqrt(x))
    s = -F(A)*G(B)
    for a in range(1, A+1):
        s += f(a)*G(x//a)
    for b in range(1, B+1):
        s += g(b)*F(x//b)
    return s

print(SIGMA2(10**15) % 10**9)