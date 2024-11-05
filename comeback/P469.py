from functools import cache

def p(n):
    #if n == 3: return 2/3
    if n < 3: return 1
    rv = 0
    for i in range(1, n-1):
        x = i * p(i) + (n-i-1) * p(n-i-1)
        rv += x / (n)
    rv = rv / (n - 2)
    return rv

# for i in range(10):
#     print(i, "->", p(i))

def E(n):
    return p(n-1) * (n-1) / n

print(E(6))

def k(n):
    if n < 3: return n
    rv = 0
    for i in range(1, n - 1):
        rv += k(i)
    return 2 * rv / (n-2)

for i in range(100):
    print(i+1, "->", k(i)/(i + 1))

print(k(5) / 6)

# E(n) converges, got steady around n = 36