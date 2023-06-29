from math import sqrt
def A(n):
    if n%5 == 0: return n
    congruency = 1
    if n%3 == 0:
        congruency*=3
        if n%9 == 0:
            congruency*=3
    ctr = 1
    t = 10
    while t != 1:
        t *= 10
        t %= (9*n)
        ctr+=1
    return ctr
def iscomposite(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0: return True
    return False
i = 91
lsum = []
while len(lsum)<25:
    if iscomposite(i):
        if (i-1)%A(i) == 0:
            lsum.append(i)
            print(i)
    i += 2
print(sum(lsum))