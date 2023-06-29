memo = dict()
def ds(len, n, first):
    if len == 0 or n == 0:
        return 1 if n == 0 else 0
    if (len, n) in memo and not first: return memo[(len, n)]
    ans = 0
    for i in range(1 if first else 0, 9):
        ans += ds(len-1, n-i, False)
    memo[(len, n)] = ans
    return ans

print(ds(16, 100, True))
