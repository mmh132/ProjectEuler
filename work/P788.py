prod = 1
for i in range(1,10**8,2):
    if i%5 != 0:
        prod *= i
        prod %= 1000000007
print(prod)