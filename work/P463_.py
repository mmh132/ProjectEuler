def f(n):
    if n == 1: return 1
    if n == 3: return 3
    if not n%2: return f(n//2)
    k=n//4
    if n%4 == 1: return 2*f(2*k+1) - f(k)
    return 3*f(2*k+1) - 2*f(k)

for i in range(1,11):
    print(i, f(i))