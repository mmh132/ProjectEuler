def CC(len):
    if len == 1: return [[1]]
    rv = []
    for i in CC(len-1):
        for k in range(1, max(i) + 2):
            if k != i[-1]:
                rv.append(i.copy() + [k])
    return rv


print(len(CC(9)))

