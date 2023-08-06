from itertools import product
from math import gcd
def g(n):
    n = list(n)
    for a in range(len(n)):
        for b in range(a+1, len(n)):
            if gcd(n[a], n[b]) > 1: return True
    return False

def bfL(n, k):
    rv = 0
    for x in product(range(1,n), repeat = k):
        if g(x):
            rv += 1
    print(rv)

bfL(10,5)