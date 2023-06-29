import math
def isRight(pts):
    x1 = pts[0][0]
    x2 = pts[1][0]
    x3 = pts[2][0]
    y1 = pts[0][1]
    y2 = pts[1][1]
    y3 = pts[2][1]
    lengths = []
    lengths.append(math.sqrt((x1-x2)**2+(y1-y2)**2))
    lengths.append(math.sqrt((x2-x3)**2+(y2-y3)**2))
    lengths.append(math.sqrt((x3-x1)**2+(y3-y1)**2))
    lengths = sorted(lengths)
    if abs(lengths[0]**2+lengths[1]**2-lengths[2]**2)<0.000001:
        return True
    return False
    

ptsets = []
def choosesets(cfrom, nchoose, out):
    if nchoose == 0:
        ptsets.append(out)
    else:
        storein = cfrom[:]
        storeout = out[:]
        for i in range(len(cfrom)):
            storein.pop(0)
            storeout.append(cfrom[i])
            choosesets(storein,nchoose-1,storeout)
            storeout = out[:]
size = 50
pts = []
coords = list(range(size+1))
for x in range(len(coords)):
    for y in range(len(coords)):
        if x!=0 or y!=0:
            pts.append([x,y])
choosesets(pts,2,[])
for i in range(len(ptsets)):
    ptsets[i].append([0,0])
print(len(ptsets))
sum = 0
for i in range(len(ptsets)):
    if isRight(ptsets[i]): sum+=1
print(sum)