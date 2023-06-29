import sys
sys.setrecursionlimit(100000)
def a(n):
    if n == 3: return 8
    else: return (3*a(n-1))**3 % 10**8
print(a(5))