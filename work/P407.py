import PrimeUtil
N = 10**3
smooth = list()
all = [2,3,5]
def dfs(n,i):
    if i == 3: 
        smooth.append(n)
        return
    while n < N:
        dfs(n, i+1)
        n*=all[i]
dfs(1,0)
print(smooth)
