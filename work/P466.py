def bf(m,n):
    rv = set()
    for i in range(1, n+1):
        for k in range(i, m*i+1, i):
            rv.add(k)
    return len(rv)

print(bf(345, 12))