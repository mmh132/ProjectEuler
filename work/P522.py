def run(l):
    l = [i-1 for i in l]
    deg = [0]*(len(l))
    for i in l:
        deg[i] += 1
    print(deg)

run([4,4,1,5,1])

def pow(n,x, m):
    rv = 1
    while x:
        if x&1:
            rv = rv*n % m
        n = n*n % m
        x >>= 1
    return rv

print(pow(2, 3, 100))