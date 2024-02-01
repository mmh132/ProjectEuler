from math import gcd

def mu(n):
    i = 2
    rv = 1
    while n > 1:
        if n%i == 0:
            n//=i
            rv *= -1
        if n%i == 0:
            return 0
        i += 1
    return rv


def divs(a):
    for i in range(1, a+1):
        if a % i == 0:
            yield i
def r(a, b):
    d = dict()
    for da in divs(a):
        for db in divs(b):
            if da*db in d:
                d[da*db] += 1
            else:
                d[da*db] = 0
    tr = []
    for i in d:
        if d[i] == 0:
            tr.append(i)
    for i in tr:
        d.pop(i)
    rv = []
    for i in d:
        rv.append((i, d[i]))
    return sorted(rv)
def magicsum(a, b):
    x = r(a,b)
    return sum([i[0]*i[1] for i in x])
def theoretical(a, b):
    g = gcd(a, b)
    x = r(g, g)
    
def d(n):
    return sum([i for i in divs(n)])


a = 5*6*2
b = 6*2
print(r(a,b),len(r(a,b)), a*b)
print(r(gcd(a,b), gcd(a,b)))
print(a,b,d(a)*d(b) - d(a*b), d(a*b//gcd(a,b)//gcd(a,b)))

# x = r(a, b)
# print(sum([i[0]*i[1] for i in x]))
# x2 = r(gcd(a, b), gcd(a, b))
# print(sum([i[0]*i[1] for i in x]), sum([i[0]*i[1] for i in x2]))

# out = 0
# for i in divs(gcd(a,b)):
#     for j in divs(gcd(a, b)):
#         if not i or not j: continue
#         print(d(a//i)*d(b//j)*magicsum(i,j), i, j)
# print(out)
# print(d(a//gcd(a, b))*d(b//gcd(a, b))*magicsum(gcd(a,b),gcd(a,b)))