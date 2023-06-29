from math import sqrt
from functools import cmp_to_key
def compare(f1,f2):
    if f1[0]*f2[1]>f2[0]*f1[1]: return 1
    elif f1[0]*f2[1]==f2[0]*f1[1]: return 0
    else: return -1
def facn(n):
    facs = []
    for i in range(2, int(sqrt(n)) + 2):
        while n%i == 0: facs.append(i); n//=i
    return [*set(facs)]
def check(n,l):
    for i in l:
        if n%i == 0: return False
    return True
def fracn(n):
    facs = facn(n)
    fracs = []
    for i in range(1,n):
        if check(i,facs):
            fracs.append((i,n))
    return fracs
alls = []
for i in range(2,12001):
    alls += fracn(i)
alls.sort(key = cmp_to_key(compare))
print(alls)
print(alls.index((1,2))-alls.index((1,3))-1)