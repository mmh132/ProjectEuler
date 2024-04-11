def bf(n):
    for i in range(0, n + 1):
        print(i, (i**3 + i + 1) % n)
    return -1

bf(7)