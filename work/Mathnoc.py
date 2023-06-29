import math
def f(x): return 8*x**2-x**5-12

def rRieman(start, end, cuts):
    inc = (end-start)/cuts
    iter = start + inc
    riemanSum = 0
    for i in range(cuts):
        riemanSum += f(iter)*inc
        iter += inc
    return riemanSum

def lRieman(start, end, cuts):
    inc = (end-start)/cuts
    iter = start 
    riemanSum = 0
    for i in range(cuts):
        riemanSum += f(iter)*inc
        iter += inc
    return riemanSum

def mRieman(start, end, cuts): 
    inc = (end-start)/cuts
    iter = start + inc/2
    riemanSum = 0
    for i in range(cuts):
        riemanSum += f(iter)*inc
        iter += inc
    return riemanSum

print(rRieman(-2,2,8))
print(lRieman(-2,2,8))
print(mRieman(-2,2,8))