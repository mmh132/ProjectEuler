def dp(l, r, s):
    rv = 0
    for i in range(1 if l else 0, s if r else s+1):
        rv += dp(l, True, i)*dp(True, r, s-i-1)
    return rv if rv>0 else 1
print(dp(False, False, 4))