from random import uniform as rand

def f():
    c1, c2 = sorted([rand(0, 1), rand(0, 1)])
    #if c1 > c2: c1, c2 = c2, c1
    if abs(c1) > 0.5 or abs(c2-c1) > 0.5 or abs(1-c2) > 0.5:
        return True
    return False

acc = 0
for i in range(100000):
    acc += 1 if f() else 0
print(acc)