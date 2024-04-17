def rev(n):
    x = n + int(str(n)[::-1])
    while x:
        if x % 2 == 0:
            return False
        x//=10
    return True

rv = 0
for i in range(1, 10**9):
    if rev(i): rv += 1
print(rv)