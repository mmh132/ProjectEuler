def factorsieve(n):
    blank = [False]
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == [False]:
            rv[i].append(i)
            rv[i][0] = True
            for k in range(i+i,len(rv),i):
                rv[k].append(i)
    return rv
def f(n):
    things = factorsieve(int(n**0.5))
    primes = [i[1] for i in things if i[0] == True]
    composites = [i for i in range(len(things)) if things[i][0] == False and i>3]
    csum = set()
    for i in primes:
        if 2**i > n: break
        for c in composites:
            if c**i < n:
                csum.add(c**i)
    return sum(csum) - 16
print(f(10**12))
    
