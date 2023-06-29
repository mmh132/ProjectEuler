def bf(n):
    def ds(n):
        rv = 0
        while n > 10:
            rv += n%10
            n//=10
        return rv+n
    t = 0
    for i in range(1,n):
        if ds(i) == ds(137*i):
            #print(i)
            t+=1
    return t
for i in range(1,8):
    print(bf(10**i))