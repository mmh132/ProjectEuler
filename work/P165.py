
cases = [0,0,0,0]
def intersect(pt1, pt2, pt3, pt4, tol):
    x1,y1 = pt1[0], pt1[1]
    x2,y2 = pt2[0], pt2[1]
    x3,y3 = pt3[0], pt3[1]
    x4,y4 = pt4[0], pt4[1]

    isVert1 = x1 == x2
    isVert2 = x3 == x4

    if isVert1 == isVert2 == True:
        if x1 != x3: return False
        
        if y1>y3>y2 or y2>y3>y1 or y1>y4>y2 or y2>y4>y1: return True
        return False

    if not isVert1:
        s1 = (y1-y2)/(x1-x2)
    
    if not isVert2:
        s2 = (y3-y4)/(x3-x4)

    if not isVert1 and not isVert2:
        if s1 == s2:
            return -s1*x1+y1 == -s2*x3+y3
        
        xSol = (-y1+y3+s1*x1-s2*x3)/(s1-s2)

        if (x1>xSol>x2 or x2>xSol>x1) and (x3>xSol>x4 or x4>xSol>x3):
            if abs(xSol-x2)>tol and abs(xSol-x1)>tol and abs(xSol-x3)>tol and abs(xSol-x4)>tol:
                return True
        return False
    
    if isVert1:
        ySol = s2*(x1-x3) + y3
        return (y1>ySol>y2 and abs(y1-ySol)>tol and abs(y2-ySol)>tol) or (y2>ySol>y1 and abs(y1-ySol)>tol and abs(y2-ySol)>tol)
        #return y1>ySol>y2 or y2>ySol>y1
    
    if isVert2:
        ySol = s1*(x3-x1) + y1
        return (y3>ySol>y4 and abs(y3-ySol)>tol and abs(y4-ySol)>tol) or (y4>ySol>y3 and abs(y3-ySol)>tol and abs(y4-ySol)>tol)
    

rng = [290797]
for i in range(20000):
    rng.append(rng[-1]**2 % 50515093)
rng.pop(0)
lines = []
for i in range(0,5000):
    lines.append([(rng[4*i] % 500, rng[4*i+1] % 500), (rng[4*i+2] % 500, rng[4*i+3] % 500)])
print(len(lines))
print(lines[0][0])
t = 0
tol = 0.005
for i in range(5000):
    for k in range(i+1, 5000):
        if intersect(lines[i][0], lines[i][1], lines[k][0], lines[k][1], tol): 
            t+=1
print(t)