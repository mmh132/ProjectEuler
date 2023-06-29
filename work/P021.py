def sumdivisors(n):
    rv = 0
    for i in range(1,n):
        if n%i==0:
            rv+=i
    if(rv == n):
        return -1
    return rv
toprint = 0
print(sumdivisors(2))
for i in range(1,10000):
    if sumdivisors(sumdivisors(i)) == i:
        toprint+=i
print(toprint)
