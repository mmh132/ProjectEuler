import math
def factorsieve(n):
    blank = []
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == []:
            rv[i].append(i)
            for k in range(i+i,len(rv),i):
                rv[k].append(i)
    return rv
def f(n):
    facs = factorsieve(n)
    pfs = []
    nums = []
    for i in range(3, len(facs), 10):
        if set(pfs).intersection(set(facs[i])) == set() and len(facs[i]) == 1:
            pfs.append(facs[i][0])

    for i in range(3, len(facs), 10):
        if set(pfs).intersection(set(facs[i])) == set():
            nums.append(facs[i])
    print(len(nums))
    rv = 0
    for i in pfs:
        rv += math.log(i)
    return rv
print(f(10**6))
