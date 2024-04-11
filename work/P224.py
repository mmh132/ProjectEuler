
# def bf(n):
#     rv = 0
#     for a in range(1, n):
#         for b in range(a, n):
#             for c in range(b, n):
#                 if a*a + b*b == c*c - 1 and a + b + c <= n:
#                     print((a,b,c))
#                     rv += 1
#     return rv

# print(bf(1000))

N = 75*10**6
alex = set()
stk = [(2,2,3)]
while stk:
    a,b,c = stk.pop(0)
    if a+b+c <= N:
        alex.add((a,b,c))
        stk.append((2*c + b - 2*a, 2*c + 2*b - a, 3*c + 2*b - 2*a))
        stk.append((2*c + b + 2*a, 2*c + 2*b + a, 3*c + 2*b + 2*a))
        stk.append((2*c - 2*b + a, 2*c - b + 2*a, 3*c - 2*b + 2*a))

print(len(alex))



