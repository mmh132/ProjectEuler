def add(la, lb):
    return [la[i] + lb[i] for i in range(len(la))]
def factor(n):
    rv = [0]*(20000)
    i = 2
    while n > 1:
        while n%i == 0:
            n//=i
            rv[i] += 1
        i+=1
    return rv

