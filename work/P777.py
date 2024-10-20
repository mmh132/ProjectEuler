from math import pi, cos

def bf(a, b):
    rv = 0
    pts = set()
    for n in range(a):
        for m in range(1,b):
            print((cos(pi * n + b * m * pi / a), cos(a * n * pi / b + m * pi - a/b * (b*19*pi / 10))), m, n, "a")
    for n in range(1,a):
        for m in range(b):
            print((cos(pi * n + b * m * pi / a + 19*b*pi/10), cos(a * n * pi / b + m * pi)), m, n, "b")
    op = [(round(i[0], 3), round(i[1], 3)) for i in pts]
    print(set(op))
    return sum([i[0]*i[0]+i[1]*i[1] for i in set(op) if i[0]**2 != 1 and i[1]**2 != 1])

print(bf(10, 7))
print(bf(2, 5))
print(bf(2, 3))