from copy import deepcopy as dc
B, W = 60, 40
empty = []
for i in range(B+1): empty.append([0]*(W+1))

def dim2polymul(a, b):
    xa, ya = len(a), len(a[0])
    xb, yb = len(b), len(b[0])
    rv = dc(empty)

    for ai in range(xa):
        for aj in range(ya):
            for bi in range(xb):
                for bj in range(yb):
                    if ai+bi <= B and aj+bj <= W:
                        rv[ai+bi][aj+bj] += a[ai][aj]*b[bi][bj]
    return rv

out = dc(empty)
out[0][0] = 1
for b in range(B+1):
    print(b)
    for w in range(W+1):
        if b == w == 0: continue
        tm = dc(empty)
        lim = W//w if b == 0 else(B//b if w == 0 else min(B//b, W//w))
        for m in range(lim + 1):
            tm[b*m][w*m] = 1
        out = dim2polymul(out, tm)
print(out[B][W])


            