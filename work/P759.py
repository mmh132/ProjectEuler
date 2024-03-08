def bf(n):
    if n == 1: return 1
    if n&1: 
        return n + 2*bf(n//2) + bf(n//2)//(n//2)
    else:
        return 2*bf(n//2)
for i in range(1, 100):
    print(i, bf(i), bf(i)/i, bin(i))

print(sum([bf(i)*bf(i) for i in range(1, 11)]))

#ways to end at k in n moves
def f(n, k):
    if n == 0:
        return 1 if k == 0 else 0
    return f(n-1, k-1) + f(n-1, k-2) + f(n-1, k-3)

print(f(6, 6))