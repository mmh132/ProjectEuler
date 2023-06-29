def factorsieve(n):
    blank = []
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == []:
            rv[i].append(i)
            for k in range(i+i,len(rv),i):
                rv[k].append(i)
            pow = 2
            while i ** pow < n:
                for k in range(i**pow,len(rv),i**pow):
                    rv[k].append(i)
                pow += 1
    return rv

def drs(n):
    if len(str(n)) == 1:
        return n
    else:
        rv = 0
        for i in str(n):
            rv += int(i)
        return drs(rv)

def prod(l):
    rv = 1
    for i in l:
        rv *= i
    return rv

cache = {1:0}
def dp(divisors):
    if prod(divisors) in cache: return cache[prod(divisors)]
    if len(divisors) == 1: return divisors[0]
    r = [drs(prod(divisors))]
    for i in range(len(divisors)):
        x = divisors.pop(i)
        r.append(drs(x) + dp(divisors))
        divisors.insert(i,x)
    rv = max(r)
    cache[prod(divisors)] = rv
    return rv



x = factorsieve(10**6-1)
s = 0
for i in range(2,len(x)):
    a = dp(x[i])
    s += a
print(s)
        


