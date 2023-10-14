def m(x):
    rv = 0
    while not x&1 and x != 0:
        x >>= 1
        rv += 1
    return rv

def choose(n,k):
    rv = 1
    for i in range(n-k+1, n+1):
        rv *= i
    for i in range(2, k+1):
        rv //=i
    return rv

def magicfunc(n):
    old = (0,0)
    for k in range(1,n):
        mm = m(choose(n,k))
        if mm > old[0]:
            old = (mm, k)
    return old



for i in range(2,101):
    print(i, magicfunc(i), bin(i))