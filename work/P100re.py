l = [[(1,1), (0,0)]]

while max(a[1] for a in l[-1]) < 10**12:
    newl = []
    for p in l[-1]:
        newl.append((3*p[0] + 2*p[1] - 2, 4*p[0] + 3*p[1] - 3))
        newl.append((3*p[0]-2*p[1], -4*p[0]+ 3*p[1]+1))
    l.append(newl)
for i in l[-1]:
    if i[1] > 10**12:
        print(i)