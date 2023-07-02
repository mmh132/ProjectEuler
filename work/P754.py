
def factorsieve(n):
    nums = []
    emp = []
    for i in range(n+1): nums.append(emp.copy())
    for i in range(2,len(nums)):
        if nums[i] == []:
            for j in range(i, len(nums), i):
                nums[j].append(i)                
    return nums
def tot(n, facs):
    div = 1
    for i in facs:
        n *= (i-1)
        n /= i
    return int(n)
def G(n):
    rv = 1
    facs = factorsieve(n)
    for i in range(2, n+1):
        exp = tot(n+1, facs[i]) - tot(i+1, facs[i])
        rv *= pow(i, exp, 1_000_000_007)
        rv %= 1_000_000_007
        if i % 257 == 0: print((i/n)*100)
    return rv % 1_000_000_007
print(G(10))
