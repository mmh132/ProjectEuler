from math import sqrt, atan2,pi
def f(pts):
    #process points into angles
    angs = []
    for pt in pts:
        #basic trig (i hope)
        angs.append((atan2(pt[1],pt[0])*180/pi + 360)%360)
    angs.sort()

    def bs(l, u, t):
        if u-l <= 1:
            return u
        x = angs[(l+u)//2]
        if x > t:
            return bs(l, (l+u)//2, t)
        else:
            return bs((l+u)//2, u, t)

    l, u = 0,0
    for p1 in range(len(angs)):
        # set up l and u
        a = angs[p1]
        target = a + 180
        l = bs(0, len(angs), target)

        