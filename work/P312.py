import sys
sys.setrecursionlimit(100000)
def a(n):
    if n == 3: return 8
    else: return (3*a(n-1))**3 % 10**8
print(a(5))


def a(n):
    rv = 1
    for i in range(n-3):
        rv = (3*rv)**3
    return rv
print(a(5), a(6), a(7))