from math import gcd
def f(n):
    if n%2 == 0: return False
    row = (n-1)//2 + 2
    sv = 3-(row%3)
    print(sv)
    print(row)
    tot = 0

    for i in range(sv, row//2, 3):
        if gcd(row,i) == 1: tot += 1
    return tot*2
print(f(12017639147))