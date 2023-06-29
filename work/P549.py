def factorsieve(n):
    blank = []
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == []:
            exp = 1
            while i ** exp < n:
                for k in range(i**exp,len(rv),i**exp):
                    rv[k].append(i)
                exp += 1
    return rv

def small(p, e):
    