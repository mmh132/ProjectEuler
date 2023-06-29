l = [[(0,1), (2,5), (0,-1), (-1,2), (-1,-2)]]


while len(set([a for a in l[-1] if a[0]>0 and a[1]>0])) < 15:
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
print(sorted(res)[14])