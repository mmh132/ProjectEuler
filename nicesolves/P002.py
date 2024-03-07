from functools import cache

@cache
def fib(n): return 1 if n < 2 else fib(n-1) + fib(n-2)

rv, i = 0, 0
while fib(i) < 4_000_000:
    if fib(i)%2 == 0: 
        rv += fib(i)
    i += 1
print(rv)