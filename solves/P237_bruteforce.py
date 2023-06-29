
inp = 10

def dp(vset, cnode):
    if cnode == (0,3):
        return 1 if len(vset) == inp*4 else 0
    
    up = (cnode[0],cnode[1]-1)
    down = (cnode[0],cnode[1]+1)
    left = (cnode[0]-1,cnode[1])
    right = (cnode[0]+1,cnode[1])

    rv = 0

    if -1<up[0]<inp and -1<up[1]<4 and up not in vset:
        vset.add(up)
        rv += dp(vset, up)
        vset.remove(up)
    
    if -1<down[0]<inp and -1<down[1]<4 and down not in vset:
        vset.add(down)
        rv += dp(vset, down)
        vset.remove(down)
    
    if -1<left[0]<inp and -1<left[1]<4 and left not in vset:
        vset.add(left)
        rv += dp(vset, left)
        vset.remove(left)
    
    if -1<right[0]<inp and -1<right[1]<4 and right not in vset:
        vset.add(right)
        rv += dp(vset, right)
        vset.remove(right)
    
    return rv

sset = set([(0,0)])
print(dp(sset, (0,0)))

for i in range(1,11):
    inp = i
    print(dp(sset, (0,0)))



