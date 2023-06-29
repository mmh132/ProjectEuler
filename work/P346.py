f1set = set()

for b in range(2,10**6):
    n = b**2+b**1+1
    while n<10**12:
        f1set.add(n)
        n = n*b+1

print(sum(f1set) + 1)