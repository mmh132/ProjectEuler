import math
def f(x): 
    #fx can be any function, the math library has all of the wierd stuff like sine and log if you need that too

    return -1*x*math.cos(x/3)

#implementing a right rieman sum
def rRieman(start, end, cuts):
    #inc is our increment, or the base of the rectangle. 
    #it is equal to the end x value minus the start x value divided by the number of cuts (which should make intuitive sense
    # because we are cutting the x region from start to end up into "cuts" slices, so dividing by cuts)
    inc = (end-start)/cuts

    #since this is a right rieman sum, we are making rectangles with the end of each interval, 
    #so we start with the given start value, plus the first increment
    iter = start + inc

    #riemanSum variable keeps track of the sum of the areas of the rectangles
    riemanSum = 0

    #iterating through exactly "cuts" rectangles
    for i in range(cuts):
        #add to our rieman sum the base times the hight of the rectangle, so f(x) as height, and inc as width
        riemanSum += f(iter)*inc
        #increment our iterator variable to the next position
        iter += inc
    #return our sum
    return riemanSum

#same as above, except that iter starts at the start index, not at the start index plus one increment
#this is because we are doing a left rieman sum, so taking the left side of each rectangle as the height
def lRieman(start, end, cuts):
    inc = (end-start)/cuts
    iter = start 
    riemanSum = 0
    for i in range(cuts):
        riemanSum += f(iter)*inc
        iter += inc
    return riemanSum

#same as above, except that iter starts at the start index plus half an increment, not at the start index plus a whole increment
#this is because we are doing a midpoint rieman sum, so taking the midpoint of each rectangle as the height
def mRieman(start, end, cuts): 
    inc = (end-start)/cuts
    iter = start + inc/2
    riemanSum = 0
    for i in range(cuts):
        riemanSum += f(iter)*inc
        iter += inc
    return riemanSum

print(rRieman(-1,3,6))
print(lRieman(-1,3,6))
print(mRieman(-1,3,6))