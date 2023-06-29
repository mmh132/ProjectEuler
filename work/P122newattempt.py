memo = dict()
def f(n):
    if n == 1: return 1
    if n in memo: return memo[n]
    ways = []
    for i in range(1,n):
        ways.append(f(n-i) + f(i) + 1)
    rv = min(ways)
    memo[n] = rv
    return rv
print(f(15))

        