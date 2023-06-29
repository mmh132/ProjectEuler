import math
def partintwo(n,max):
    if max>n:
        return int(n/2)
    else:
        return int(n/2)-abs(max-n)
def posfora(a):
    rv = 0
    stor = 0
    for b in range(1,2*a+1):
        stor = math.sqrt(a**2+b**2)
        if stor - int(stor) == 0:
            if b<a:
                rv+=1
            rv+=partintwo(b,a)     
    return rv
sum = 0
ctr = 1
while sum<1000000:
    sum+=posfora(ctr)
    ctr+=1
print(ctr)



