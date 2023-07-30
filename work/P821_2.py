def magicfunc(n):
    t = 1 if n > 5 else 0
    for p in range(2, n, 3):
        if 6*2**p <= n:
            t += 1
        if 6*3**p <= n:
            t += 1
        if 6*2**p >= n:
            break
    #print(n, t)
    print(n, t, aaa(n))
    return min(t, aaa(n))

def aaa(n):
    t = 0
    for p in range(2, n, 3):
        if 2**(p+1) <= n:
            t += 1
        if 2*3**p <= n:
            t += 1
        if 2**p >= n:
            break
    return t

# def bigsol(n):
#     t = 0
#     for i in range(n//6):
#         t += magicfunc(n//(6*i+1))
#         t += magicfunc(n//(6*i+5))
#     if 6*(n//6) + 1 <= n:
#         t += magicfunc(n//(6*(n//6)+1))
#     if 6*(n//6) + 5 <= n:
#         t += magicfunc(n//(6*(n//6)+5))
#     return n-t
# print(bigsol(10**6))

def bigsol2(n):
    t = 0
    for i in range(1, n+1):
        if i%6 == 1 or i%6 == 5:
            t += magicfunc(n//i)
    return n-t
print(bigsol2(10**3))