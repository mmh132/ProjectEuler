def bf(sl, nl):
    if nl == 0: return 1
    rv = 0
    for i in range(min(sl+1,nl) + 1):
        rv += bf(sl+1, nl-i-1)
    return rv
print(bf(0,7))