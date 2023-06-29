inp = 100000000
import time
timer = time.time()
def factorsieve(n):
    blank = []
    rv = [blank.copy() for x in range(n+1)]
    for i in range(2,len(rv)):
        if rv[i] == []:
            rv[i].append(i)
            for k in range(i+i,len(rv),i):
                rv[k].append(i)
    return rv
def tri(n): return ((n)*(n+1))//(2)
def phi(val,n):
    tot = val
    div = 1
    for i in n:
        tot*=(i-1)
        div*=i
    print(val,n,tot//div)
    return tot//div
things = factorsieve(inp)
tot = 1
for i in range(2,len(things)):
    tot+=phi(i,things[i])
tot = tri(inp)-tot
print(tot*6)