

def masks(old, k):
    if len(old) == k:
        #print(old)
        return 1
    rv = 0
    for i in range(1, max(list(old) + [0]) + 2):
        rv += masks(tuple(list(old) + [i]), k)
    return rv


print(masks(tuple(), 10))