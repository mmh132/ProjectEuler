from math import sqrt

def factor(n):
    facs = []
    for i in range(1, int(sqrt(n)) + 1):
        if n%i == 0:
            facs.append((i, n//i))
    return facs

def sqfacs(n):
    facs = factor(n)
    new = set()
    for a in facs:
        for b in facs:
            new.add((a[0]*b[0], a[1]*b[1]))
    return new

print(sqfacs(36))
