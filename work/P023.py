def isabundant(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum+=i
    if sum>n:
        return True
    return False

abundantNums = []
for i in range(2,28123):
    if isabundant(i):
        abundantNums.append(i)
print(abundantNums)
ptr = 0
found = False

foundnums = list(range(0,28124))
for a in range(len(abundantNums)):
    for b in range(a, len(abundantNums)):
        if abundantNums[a] + abundantNums[b] < len(foundnums):
            foundnums[abundantNums[a] + abundantNums[b]] = 0
print(sum(foundnums))
