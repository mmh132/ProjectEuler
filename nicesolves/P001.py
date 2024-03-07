N = 1000-1 
def tri(n):
    return n*(n+1)//2
print(3*tri(N//3) + 5*tri(N//5) - 15*tri(N//15))