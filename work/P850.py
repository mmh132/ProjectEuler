def bf(n, k):
    x = 0
    for i in range(1, n+1):
        x += pow(i, k)%n
    return x/n
#print(bf(1234, 7))

def bfS(n):
    x = 0
    for k in range(1, n+1,2):
        for nn in range(1, n+1):
            for i in range(1, nn+1):
                x += pow(i,k,nn)/nn
    return x

def altS(n):
    x = 0
    for k in range(1, n+1, 2):
        for i in range(1, n+1):
            for nn in range(i, n+1):
                x += pow(i,k,nn)/nn
    return x
# print(bfS(10))
# print(altS(10))


def tv(n):
    print([[i**k % n for i in range(1, n)] + ["pow =" + str(k)] for k in range(1, 12)])

for i in range(5, 14):
    print(str(i))
    print(tv(i))
    print(" ")
    
