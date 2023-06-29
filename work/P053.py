def factorial(n):
    if n == 0 or n == 1:
        return 1
    for i in range(2,n):
        n=n*i
    return n

def choose(n,k):
    if k == 0:
        return 1
    return factorial(n)/(factorial(n-k)*factorial(k))

sum = 0
for n in range(1,101):
    for r in range(1,n+1):
        if choose(n,r)>1000000:sum+=1
        print(n)

print(sum)
