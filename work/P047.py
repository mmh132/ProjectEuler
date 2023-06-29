def primefactorn(n):
    listfacs = []
    i = 2
    while n!=1:
        while n%i == 0: listfacs.append(i); n=n/i
        i+=1
    rv = 0
    thing = []
    for i in listfacs:
        if i not in thing:
            rv+=1
            thing.append(i)
    return rv
print(primefactorn(4023))
c1,c2,c3,c4 = 0,0,0,0
i = 1 
go = True
while go == True:
    c1 = c2
    c2 = c3
    c3 = c4
    c4 = primefactorn(i)
    i+=1
    if c1 == c2 == c3 == c4 == 4: 
        print(i-4)
        go=False