r = []
def rblists(l):
    if len(l) == 4: r.append(l); return
    for i in range(0,10): rblists(l + [i])
rblists([])
a = []
indices = [a.copy() for k in range(37)]
for i in range(len(r)):
    indices[sum(r[i])].append(i)
def check(l1,l2,l3,l4,size):
    for i in range(4):
        if l1[i] + l2[i] + l3[i] + l4[i] != size: return False
    if l1[0] + l2[1] + l3[2] + l4[3] != size: return False
    if l1[3] + l2[2] + l3[1] + l4[0] != size: return False
    return True
tot = 0
for size in range(0,37):
    print(size)
    for l1 in indices[size]:
        for l2 in indices[size]:
            for l3 in indices[size]:
                for l4 in indices[size]:
                    if check(r[l1],r[l2],r[l3],r[l4],size):
                        tot += 1
print(tot)