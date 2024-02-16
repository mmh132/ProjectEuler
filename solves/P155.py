from fractions import Fraction
N = 18
x = set()
dp = [x.copy() for _ in range(N+1)]
dp[1].add(Fraction(1,1))
for i in range(2, N+1):
    print(i)
    for j in range(1, i+1):
        for x in dp[j]:
            for y in dp[i-j]:
                dp[i].add(x + y)
                dp[i].add(x*y/(x+y))
t = set()
for i in range(1, N + 1):
    for j in dp[i]:
        t.add(j)
print(len(t))