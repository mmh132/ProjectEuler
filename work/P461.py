from math import exp, log, pi
from bisect import bisect_left
def g(n):
    lim = int(log(1+pi)*n)
    vals = [(exp(k/n) - 1, k) for k in range(lim+1)]

    pairs = []
    for a in vals:
        for b in vals:
            pairs.append((a[0] + b[0], a[1]*a[1]+b[1]*b[1]))
    
    pairs.sort()
    berr = 4
    bum = 123123
    for i in pairs:
        p = bisect_left(pairs, (pi-i[0], None))-1
        if 0 < pi - pairs[p][0] - i[0] < berr:
            berr = pi-pairs[p][0]-i[0]
            bum = pairs[p][1] + i[1]
    return bum

print(g(10000))
    


