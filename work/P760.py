def testadd(a,b):
    x = a&b
    y = a^b
    return x+y

for a in range(1, 8):
    for b in range(1, 8):
        print(a, b, testadd(a,b))

def g(a,b):
    x = a&b
    y = a^b
    z = a|b
    return x+y+z

def G(n):
    t=0
    for i in range(n+1):
        for j in range(0, i+1):
            t += g(j, i-j)
    return t

print(G(10))
print(6&4)
print(6^4)