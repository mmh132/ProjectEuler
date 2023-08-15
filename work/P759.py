def bf(n):
    if n == 1: return 1
    if n&1: 
        return n + 2*bf(n//2) + bf(n//2)//(n//2)
    else:
        return 2*bf(n//2)
for i in range(1, 100):
    print(i, bf(i), bf(i)/i, bin(i))

for i in range(1, 50):
    print(i, bin(i), i*i, bin(i*i))