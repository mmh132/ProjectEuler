def roots(m):
    rv = set()
    for i in range(1, m):
        if i**3%m == 1:
            rv.add(i)
    return rv
print(roots(7))
print(roots(13))
print(7*13)