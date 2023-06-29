from math import ceil as ceil
def primefactorn(n):
    listfacs = []
    i = 2
    while n!=1:
        while n%i == 0: listfacs.append(i); n=n/i
        i+=1
    return listfacs
def invdipsolns(n):
    listfacs = primefactorn(n)
    absnums = [1]
    for i in range(len(listfacs)-1):
        if listfacs[i] == listfacs[i+1]: absnums[-1]+=1
        else: absnums.append(1); 
    solns = 1
    for i in range(len(absnums)): solns*=(absnums[i]*2 + 1)
    return ceil(solns/2)

i = 10
thing = invdipsolns(i)
while thing<1000:
    i += 1
    if i%5 == i%7 == i%2 == i%3 == 0:
        thing = invdipsolns(i)
print(i)
print(primefactorn(9350130049860600))

i = 1
thing = invdipsolns(i)
while thing<4000000:
    i += 1
    thing = invdipsolns(2*2*2*3*3*5*7*11*13*17*19*23*29*i)
print(i*2*2*2*3*3*5*7*11*13*17*19*23*29)