def sqrep(n):
    s = 0
    for a in range(1, n):
        for b in range(a, n):
            if a**2 + b**2 == n:
                s += 1
                print(a,b)
            if a **2 + b**2 > n:
                break
    return s

print(sqrep(5*13*7*7))