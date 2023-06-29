rows = []
def rowmaker(size, l):
    if size == 0: rows.append(l); return
    else: 
        if l[-1] == 0:
            rowmaker(size-1, l+[1])
            rowmaker(size-1, l+[0])
        else: 
            rowmaker(size-1, l+[0])
            for i in range(1,len(l)+1):
                if l[-i] > 0: l[-i] += 1
                else: break
            rowmaker(size-1, l + [l[-1]])
rowmaker(2, [0])
rowmaker(2,[1])
print(rows)
def super(rowa, rowb):
    for i in range(len(rowa)):
        if rowb[i] != 0: rowb[i] += rowa[i]
    for i in range(len(rowb)-1):
        if rowb[i] != 0 and rowb[i+1] != 0: rowb[i] = rowb[i] + rowb[i+1]; rowb[i+1] = rowb[i]
    return rowb
a = [0,2,0]
b = [3,3,3]
print(super(a,b))
#def rb(prow, max):

