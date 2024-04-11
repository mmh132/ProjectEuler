from math import comb

def sump(a, n):
    rv = 0
    for i in range(n + 1):
        rv += a**i
    return rv

def I(k, n):
    rv = 0
    for i in range(k):
        rv += (-1) ** (k-i + 1) * comb(k, i) * sump(i, n)
    return rv

print(I(3, 2))

def s1(a, n):
    rv = 0
    for j in range(1, a+1):
        for i in range(0, j):
            print(i, j)
            rv += ((-1) ** (j-i+1)) * sump(i, n) * comb(j, i)
    return rv

def s2(a, n):
    rv = 0
    for i in range(0, a):
        for j in range(i+1, a+1):
            print(i, j)
            rv += ((-1) ** (j-i+1)) * sump(i, n) * comb(j, i)
    return rv


print(s1(4, 4))
print("------------")
print(s2(4, 4))