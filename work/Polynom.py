def evaluatePoly(polynom, x):
    rv = 0
    for i in range(len(polynom)):
        rv += polynom[i]*(x**i)
    return rv

def sumPoly(inPoly):
    #degree of polynomial is length of input-1 (remove constant term)
    degree = len(inPoly)-1
    
    #create storage for the polynomial that represents the sum
    sumPolyCoef = [0]*(len(inPoly) + 1)

    #horners method for evaluating polynomial at degree + 1
    evaluate = inPoly
    return

print(evaluatePoly([3,2,1], 4))


