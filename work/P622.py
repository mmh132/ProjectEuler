from math import lcm

def bf(n):
    if n&1:
        return -1
    l = [0]*n
    l[::2] = list(range(n//2))
    l[1::2] = list(range(n//2, n))
    c = 1
    for i in range(len(l)):
        x = 1
        s = l[i]
        l[i] = -1
        while l[s] != -1:
            os = s
            s = l[s]
            l[os] = -1
            x += 1
        c = lcm(x, c)
    return c

print([bf(i) for i in range(0, 20, 2)])