def f(x):
    return int(pow(2, 30.403243784-x**2))*(10**-9)

seq = [-1, f(-1)]
while len(seq) < 10000:
    seq.append(f(seq[-1]))
    print(seq[-1])
print(seq[-1] + seq[-2])
