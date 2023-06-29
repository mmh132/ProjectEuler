import math
def isNice(n):
    while n%2 == 0: n//=2
    while n%5 == 0: n//=5
    return n == 1
s = 0
for i in range(5, 101):
    d = round(i/math.e)
    s += i * (-1 if isNice(d // math.gcd(i,d)) else 1)
print(s)