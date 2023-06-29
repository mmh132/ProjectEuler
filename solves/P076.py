memo = dict()
def part(n,k):
    if n == k and k == 0: return 1
    if n<1 or k<1: return 0
    if (n,k) in memo: return memo[n,k]
    rv = part(n-1,k-1) + part(n-k, k)
    memo[(n,k)] = rv
    return rv
num = 100
toprint = 0
for i in range(1, num+1):
    toprint += part(num, i)
print(toprint-1)