from math import lcm

def listLcm(l):
    rv = 1
    for i in l:
        rv = lcm(rv, i)
    return rv

print(listLcm([1,2,3,4,5]))