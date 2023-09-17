def factorizations(n):
    if n == 1: 
        return 1
    rv = 0
    for i in range(2, n + 1):
        if n%i == 0:
            rv += factorizations(n//i)
    return rv

print(factorizations(54))