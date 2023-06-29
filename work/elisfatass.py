import Fibonacci

def fisb(n, mod):
    n-=2
    c1,c2,c3 = 1,1,2
    for i in range(n):
        c1 = c2
        c2 = c3 
        c3 = c1+c2 % mod
    return c3

#print(fisb(10**9, 123456789))

print(Fibonacci.fib(10**100, 6942069420))

21