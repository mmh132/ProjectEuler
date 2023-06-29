from math import gcd as g
import math


def recfrac(num, denomroot, denomreal, iters):
    if iters == 0: return
    newtop = (denomroot-denomreal**2)/num
    newbase = denomroot - math.floor((math.sqrt(denomroot) + denomreal)/newtop)
    print(math.floor((math.sqrt(denomroot) + denomreal)/newbase))
    recfrac(newbase,denomroot,newtop,iters-1)
recfrac(1,23,4,5)
