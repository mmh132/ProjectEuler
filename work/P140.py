l = [[(0,3),(2,5),(4,-9),(4,9),(2,-5),(0,-3),(-5,12),(-1,-4),(-1,4),(-5,-12)]]

#currently wrong recurrence
for i in range(20):
    newl = []
    for p in l[-1]:
        newl.append((-9*p[0] + 4*p[1] - 2, 20*p[0] - 9*p[1] + 4))
        newl.append((-9*p[0] - 4*p[1] - 2, -20*p[0] - 9*p[1] - 4))
    l.append(newl)
res = []
for a in l:
    for b in a:
        if b[0]>0 and b[1]>0 and b[0] not in res:
            res.append(b[0])
print(res)
print(211345365 in res)
print(sorted(res)[19])