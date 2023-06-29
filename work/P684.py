
def S(n):
    rv = -n
    for x in range(1, n+1):
        rv += (x%9 + 1)*pow(10, x//9)
    return rv


fib = [0,1]
while len(fib) < 91:
    fib.append(fib[-1] + fib[-2]) 
fib.pop(0)
fib.pop(0)


def o(x, r):
    return (x-r+9)//9 - (1 if r == 0 else 0)

def sumten(x, mod):
    a = pow(10, x, mod)
    b = pow(10-1, -1, mod)
    return ((a-1)*b) % mod

def f(x):
    rv = -x
    rv += sumten(o(x,0) + 1, 10**9+7) - 1
    for r in range(1, 9):
        rv += (r+1)*(sumten(o(x, r), 10**9+7))
    rv %= 10**9+7
    return rv

s = 0
for i in fib:
    s += f(i)
print(s % (10**9+7))


