def gcd(a, b):
    if a < b: a,b = b,a
    while b:
        a, b = b, a%b
    return a

def ctdiv(n):
    return sum(1 if not n%i else 0 for i in range(1, n+1))

def alt(i, j):
    rv = 0
    for d in range(1, gcd(i, j)+1):
        if not gcd(i, j) % d:
            rv += ctdiv(i*j//d//d)
    return rv
