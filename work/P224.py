N = 75_000_000
alex = set()
stk = [(2,2,3)]
while stk:
    a,b,c = stk.pop(0)
    if 2*c + b - 2*a + 2*c + 2*b - a + 3*c + 2*b - 2*a <= N:
        stk.append((2*c + b - 2*a, 2*c + 2*b - a, 3*c + 2*b - 2*a))
    if 2*c + b + 2*a + 2*c + 2*b + a + 3*c + 2*b + 2*a <= N:
        stk.append((2*c + b + 2*a, 2*c + 2*b + a, 3*c + 2*b + 2*a))
    if 2*c - 2*b + a + 2*c - b + 2*a + 3*c - 2*b + 2*a <=N:
        stk.append((2*c - 2*b + a, 2*c - b + 2*a, 3*c - 2*b + 2*a))
    alex.add((a,b,c))

print(len(alex))
