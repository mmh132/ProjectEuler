def testsubset(numbers):
    allnums = [0]*(sum(numbers)+1)
    allnums[0] = 1
    for x in numbers:
        temp = allnums.copy()
        for i in range(len(allnums)):
            if temp[i] != 0:
                if allnums[i+x] == 0: allnums[i+x] += temp[i]+1
                else: return False
    cur = 0
    for i in range(len(allnums)):
        if allnums[i] != 0:
            if allnums[i] < cur: return False
            else: cur = allnums[i]
    return True
cap = 50
best = 1000000
for e1 in range(19,cap):
    for e2 in range(e1, cap):
        for e3 in range(e2, cap):
            for e4 in range(e3, cap):
                for e5 in range(e4, cap):
                    for e6 in range(e5, cap):
                        for e7 in range(e6, cap):
                            if e7<44: continue
                            if testsubset([e1,e2,e3,e4,e5,e6,e7]):
                                if sum([e1,e2,e3,e4,e5,e6,e7]) < best:
                                    best = sum([e1,e2,e3,e4,e5,e6,e7])
                                    print([e1,e2,e3,e4,e5,e6,e7])
