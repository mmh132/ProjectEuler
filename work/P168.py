
def ton(l):
    rv = 0
    for i in range(len(l)): rv += l[i] * 10**i
    return rv

def s(n):
    if len(n) < 2 or n[-1] == 0: return 0
    x = ton(n)
    f = n.pop(0)
    y = ton(n + [f])
    return x % 10**6 if y%x == 0 else 0

def dp(fd, m, r, n):
    if len(n)>100: return 0

    rv = 0 if r else s(n.copy())
    return rv + dp((fd * m + r) % 10, m, (fd * m + r)//10, n + [fd])

dp(7, 5, 0, [])

out = 0
for i in range(10):
    for j in range(10):
        out += dp(j, i, 0, [])
print(out % 10**6)




