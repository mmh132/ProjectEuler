def A(n):
    if n%5 == 0: return 1
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
print(A(41))

k = 1000001
while A(k)<1000000:
    k+=2
    print(k)
print(k)