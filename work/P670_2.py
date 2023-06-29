def f(n, t, b, m):
    while t > 0 and b > 0:
        t -= 1
        b -= 1
        n -= 1

    if n == 0:
        return 1 if t == b == 0 else 0
    
    if n < 0:
        return 0
    
    rv = 0
    if t == b:
        rv += (3 if m else 2) * f(n-1, t, b, True)
        for i in range(1,4):
            rv += 3*f(n, t+i, b, False)
    else:
        for i in range(1, 4):
            rv += 3*f(n, max(t, b+i), min(t, b+i), False)
    
    return rv

inp = 2
out = 0
out += 4*f(inp-1, 0, 0, True)
for i in range(1, 4):
    out += 4*f(inp, i, 0, False)
print(out)