from Frac import fraction
cases = [0,0,0,0]


def intersect(pt1, pt2, pt3, pt4):
    x1,y1 = fraction(pt1[0],1), fraction(pt1[1],1)
    x2,y2 = fraction(pt2[0],1), fraction(pt2[1],1)
    x3,y3 = fraction(pt3[0],1), fraction(pt3[1],1)
    x4,y4 = fraction(pt4[0],1), fraction(pt4[1],1)

    isVert1 = x1 == x2
    isVert2 = x3 == x4

    if isVert1 == isVert2 == True:
        return False

    if not isVert1:
        s1 = (y1-y2)/(x1-x2)
    
    if not isVert2:
        s2 = (y3-y4)/(x3-x4)

    if not isVert1 and not isVert2:
        if s1 == s2:
            return False
        
        xSol = (-y1+y3+s1*x1-s2*x3)/(s1-s2)

        if (x1>xSol>x2 or x2>xSol>x1) and (x3>xSol>x4 or x4>xSol>x3):
            return True
        return False
    
    if isVert1:
        ySol = s2*(x1-x3) + y3
        return (y1>ySol>y2) or (y2>ySol>y1)
    
    if isVert2:
        ySol = s1*(x3-x1) + y1
        return (y3>ySol>y4) or (y4>ySol>y3)
    

rng = [290797]
for i in range(20000):
    rng.append(rng[-1]**2 % 50515093)
rng.pop(0)
lines = []
for i in range(0,5000):
    lines.append([(rng[4*i] % 500, rng[4*i+1] % 500), (rng[4*i+2] % 500, rng[4*i+3] % 500)])
print(lines[0], lines[1])
t = 0
for i in range(5000):
    #print(i)
    for k in range(i+1, 5000):
        if intersect(lines[i][0], lines[i][1], lines[k][0], lines[k][1]): 
            t+=1
print(t)