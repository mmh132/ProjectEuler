from math import gcd
def bfF(l):
    rv = 0
    for i in range(1, l):
        for j in range(i+1, l+1):
            if i*j % (i+j) == 0:
                rv += 1
                print(i,j,gcd(i,j))
    return rv

print(bfF(50))

def firstsum(n):


def secondsum(n):
    