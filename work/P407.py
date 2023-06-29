def isqrt(x):
    if x == 1: return 1
    a = x >> 1
    b = x
    while a < b:
        c = (a + x//a) >> 1
        a,b = c,a
    return b

def M(n):
    b = 1
    for i in range(1, isqrt(n) + 1):
        x = i*i
        if (x*x) % n == x:
            b=x
    return b

print(sum(M(n) for n in range(1, 10**5+1)))

def bfm(n):
    b = 1
    for i in range(1, n):
        if i*i % n == i:
            b = i
    return b

for i in range(1, 1000):
    if bfm(i) != M(i):
        print(i, bfm(i), M(i))