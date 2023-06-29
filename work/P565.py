def S(n, m):
    div = [1]*(n+1)
    for i in range(2, n+1):
        for k in range(i, n+1, i):
            div[k] += i
            div[k] %= m
    sum = 0
    for i in range(len(div)):
        if div[i] == 0: 
            sum += i
            print(i)
    return sum
print(S(10**6, 2017))