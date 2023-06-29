def factor(n):
    pfs = []
    for i in range(2, n):
        toap = 0
        while n%i == 0:
            n//=i
            toap += 1
        if toap != 0:
            pfs.append((i, toap))
    return pfs

def mob(n):
    facs = factor(n)
    angry = 0
    k1 = 0
    k3 = 0
    for i in facs:
        if i[0] % 4 == 3:
            k3 += 1
            if i[1] > 1:
                if i[1] > 3:
                    return 0
                angry += 1
        else:
            k1 += 1
            if i[1] > 1:
                return 0
    if angry > 1:
        return 0
    print(k1, k3)

memo = dict()
def f(n):
    if n in memo: return memo[n]
    t = (n-1)//4 + 1
    rv = t
    for k in range(3, int(t**0.5), 2):
        rv -= f(t//(k*k))
    memo[n] = rv
    return rv

print(f(10**7))

    
    
