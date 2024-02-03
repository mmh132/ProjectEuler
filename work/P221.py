N = 12
alex = set()
stk = [(3,1,2)]
while stk and len(alex) < N:
    a,b,c = stk.pop(0)
    if a*b*c < 0: continue
    stk.append((2*c + b - 2*a, 2*c + 2*b - a, 3*c + 2*b - 2*a))
    stk.append((2*c + b + 2*a, 2*c + 2*b + a, 3*c + 2*b + 2*a))
    stk.append((2*c - 2*b + a, 2*c - b + 2*a, 3*c - 2*b + 2*a))
    alex.add(a*b*c)

print(alex)