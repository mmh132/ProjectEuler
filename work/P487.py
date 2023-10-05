def f(k,n):
    return sum(i**k for i in range(n+1))
def s(k,n):
    return sum(f(k,i) for i in range(1, n+1))
print(s(4,100))