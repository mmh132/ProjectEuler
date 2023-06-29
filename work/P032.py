def checkpandigital(list):
    return sorted(list) == [str(i) for i in range(1,10)]
def check(n):
    l = list(str(n))
    if len(l) != len([*set(l)]): return False
    for i in range(1,n):
        if n%i == 0:
            temp = l.copy()
            temp += list(str(i))
            temp += list(str(n//i))
            if checkpandigital(temp): return True
    return False
tot = 0
for i in range(1000, 9999):
    if check(i):
        print(i)
        tot+=i
print(tot)