from functools import cache 
import sys
sys.setrecursionlimit(100000)


def f(a, b, c):
    if a < 1 or b < 1 or c < 1:
        print(a, b, c)
        return 0
    
    if a == b: return 3
    if a == c: return 2
    if b == c: return 1

    if a == b + c:
        s = f(abs(b - c), b, c)
        p = (s % 3) if (s % 3) else 3
        if p == 2:
            return s + 2
        if p == 3:
            return s + 1
        print((a, b, c), s, "fuck")
        return "fuck"

    if b == a + c:
        s = f(a, abs(c - a), c)
        p = (s % 3) if (s % 3) else 3 
        if p == 1:
            return s + 1
        if p == 3:
            return s + 2
        print((a, b, c), s, "fuck")
        return "fuck"

    if c == a + b:
        s = f(a, b, abs(a - b))
        p = (s % 3) if (s % 3) else 3
        if p == 1: 
            return s + 2
        if p == 2: 
            return s + 1
        print((a, b, c), s, "fuck")
        return "fuck"

    return "fuck"

rv = 0
for a in range(1, 8):
    for b in range(1, 20):
        print(a, b)
        rv += f(a**b, b**a, a**b + b**a)
        print(rv)
