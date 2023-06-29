s = 0
for i in range(1,10):
    pow = 1
    x = i
    while pow <= len(str(x)):
        if len(str(x)) == pow:
            s += 1
        x *= i
        pow += 1
print(s)
