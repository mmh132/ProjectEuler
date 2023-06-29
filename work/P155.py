n = 18
a = [1]
while len(a) < n:
    a.append(a[-1] * 2)
print(a)
print(sum(a))