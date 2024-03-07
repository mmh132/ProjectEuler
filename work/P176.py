

def test(n):
    rv = 0
    for i in range(1, n):
        if n*n % i == 0:
            if not n*n//i + i & 1:
                rv += 1
    return rv

print(test(12))