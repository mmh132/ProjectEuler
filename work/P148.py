
def tb(n, b):
    rv = []
    while n:
        rv.append(n % b)
        n//=b
    return rv

def row(n):
    rv = 1
    for i in tb(n, 7):
        rv *= 1 + i
    return rv

tp = 1
for i in range(1, 10**9):
    if not i % 10**6: print(i / 10**7)
    tp += row(i)
print(tp)