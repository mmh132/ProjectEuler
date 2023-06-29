from math import floor as flo
def pent(n):
    return (n*(3*n-1))//2
def gsubk(n):
    if n%2 == 0: return pent(n/2)
    else: return pent(-flo(n/2))
i = 2
pentagonals = []
while i < 100000:
    pentagonals.append(int(gsubk(i)))
    i+=1
ps = dict()
def part(n):
    if n == 1: return 1
    if n<1: return 0
    if n in ps: return ps[n]
    i = 0
    rv = 0
    while pentagonals[i]<n:
        if i%4 in [2,3]: rv += -1*part(n-pentagonals[i])
        else: rv += 1*part(n-pentagonals[i])
        i+=1
    ps[n] = rv
    return rv
i = 1
thing = part(i)
while thing%1000000 != 0:
    i+=1
    print(i-1)
    thing=part(i)

