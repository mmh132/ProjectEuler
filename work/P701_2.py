S = 4
def combine(r1, r2):
    row = r2.copy()
    for i in range(S):
        if r1[i] != 0 and r2[i] != 0:
            toad = r1[i]
            for k in range(i, S):
                if r1[k] != 0:
                    if i == 0:
                        r1[k] = 0
                    if r2[k-1] != 0:
                        r1[k] = 0
                else:
                    break
            for k in range(i, S):
                if r2[k] != 0:
                    row[k] += toad
                else:
                    break
            for k in range(i-1, -1, -1):
                if r2[k] != 0:
                    row[k] += toad
                else:
                    break
    return row

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
    
memo = dict()
def dp(state, m, l):
    if l == S:
        if m == 16: 
            print(state, m)
        return m
    if tuple(state + [m,l]) in memo: return memo[tuple(state + [m,l])]
    rv = 0
    for i in rows:
        x = combine(state.copy(), i.copy())
        if 16 in state or 16 in i or 16 in x:
           print(state, i, x)
        rv += dp(x, max(m, max(x)), l+1)
    memo[tuple(state + [m,l])] = rv
    return rv
rowmaker(S-1, [0])
rowmaker(S-1, [1])
#print(rows)
aargh = dp([0]*S, 0, 0)
for i in range(S*S):
    aargh/=2
print(aargh)
            

