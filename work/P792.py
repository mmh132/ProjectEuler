from math import comb

def S(n):
    rv = 0
    for i in range(1, n + 1):
        rv += pow(-2, i) * comb(2*i, i)
    return rv

def u(n):
    rv, x = 0, 3*S(n) + 4
    print(x)
    while not x%2:
        rv += 1
        x //= 2
    return rv

print([u(i) for i in range(1, 11)])