def a(n):
    if n == 1:
        return 1
    return a(n-1) + 7*b(n-1)

def b(n):
    if n == 1:
        return 1
    return a(n-1) + b(n-1)

# for i in range(1,12):
#     print(a(i))

#a(n) = 2*a(n-1) + 6*a(n-2) with a(0) = a(1) = 1

# for i in range(1, 12):
#     print(b(i))

#b(n) = 2*b(n-1) + 6*b(n-2) with b(0) = 0 and b(1) = 1