def sieve(n):
    numbers = list(range(1,n+1))
    solns = []
    for i in range(n):
        solns.append([1])
    ctr = 1
    for i in range(2,len(numbers)+1):
        for j in range(i-1,len(numbers),i):
            solns[j].append(i)
    return solns
def solns(n):
    z3i = 0
    c = 0
    rv = 0  
    founds = []
    for i in range(len(factors[n-1])):
        z3i = n/factors[n-1][i]
        if (z3i+factors[n-1][i])%4 == 0:
            c=(z3i+factors[n-1][i])/4
            if z3i-3*c<0:
                rv+=1
    return rv          
total = 0
factors = sieve(1000000)
for i in range(len(factors)):
    if solns(i) == 10:
        total+=1
print(total)

