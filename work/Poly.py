import math
def eval(p, x):
    rv = 0
    for exp, coef in enumerate(p):
        rv += coef*pow(x, exp)
    return rv

def mult(p1, p2):
    rv = [0]*(len(p1) + len(p2)-1)
    for n1, c1 in enumerate(p1):
        for n2, c2 in enumerate(p2):
            rv[n1+n2] += c1*c2
    return rv

def add(p1, p2):
    if len(p2)>len(p1): return add(p2, p1)
    for idx, i in enumerate(p2):
        p1[idx] += i
    return p1

def interpolate(pttpls):
    rp = [0]*len(pttpls)
    for pair in pttpls:
        cp = [1]
        den = 1
        for opair in pttpls:
            if pair != opair:
                den*= (pair[0]-opair[0])
                cp = mult(cp, [-opair[0], 1])
        t = [i*pair[1] for i in cp]
        cp = [i/den for i in t]
        rp = add(cp, rp)
    return [i for i in rp]

def printpoly(polynom):
    rv = "y = "
    a = polynom.pop(0)
    rv += str(a) + " "
    for exp, coef in enumerate(polynom):
        rv += "+ (" + str(coef)
        rv += "*x^"
        rv += str(exp+1)
        rv += ") "
    print(rv)
    return

printpoly([1,-2,3])

pts = [(1,3), (2,7), (8,15), (14,10), (10,20)]

printpoly(interpolate(pts))