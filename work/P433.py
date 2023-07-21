def gcd(x, y, s):
    if y == 0: return (x, s)
    xn, yn = y, x%y
    return gcd(xn, yn, s+1)

print(gcd(10, 6, 0))
print(gcd(6, 10, 0))

print(gcd(7, 5, 0))
print(gcd(13, 11, 0))
print(gcd(11, 5, 0))