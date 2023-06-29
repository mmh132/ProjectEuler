l = [[(-2, 1), (0,0) , (-2,0) , (0,1) ]]


for i in range(20):
    newl = []
    for p in l[-1]:
        newl.append((3*p[0] + 2*p[1] + 1, 4*p[0] + 3*p[1] + 3))
        newl.append((3*p[0] - 2*p[1] + 3, -4*p[0] + 3*p[1] - 5))
    l.append(newl)
res = []
for a in l:
    for b in a:
        if b[0]>0 and b[1]>0 and b[0] not in res:
            res.append(b[0])
res.sort()
print(sum(res[i] for i in range(40)))