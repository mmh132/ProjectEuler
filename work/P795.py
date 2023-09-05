from math import gcd
def g(n):
    rv = 0
    for i in range(1, n+1):
        rv += pow(-1, i)*gcd(i*i, n)
    return rv

for i in range(1,1000):
    if i&1: 
        if g(i) > 0:
            print(i, g(i))
    else:
        if g(i) < 0:
            print(i, g(i))

p=67
print(g(p))
print(g(2*p))
print(g(2*2*p))
print(g(2*2*2*p))
print(g(2*2*2*2*p))
print(144*p - 72)