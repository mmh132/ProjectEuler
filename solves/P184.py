from math import tan, sqrt
def sortpts(pts):
    polar = [(tan(i[1]/i[0]), sqrt(i[0]*i[0] + i[1]*i[1])) for i in pts]
    def merge(l1, l2):
        rl = []
        o = str(l1) + str(l2)
        while l1 and l2:
            if l1[0] < l2[0]:
                rl.append(l1.pop(0))
            else:
                rl.append(l2.pop(0))
        o += str(rl)
        print(o)
        return l1 + rl
    def sort(l):
        if len(l) <= 1: return l
        return merge(sort(l[len(l)//2:]), sort(l[:len(l)//2 - 1 if len(l)&1 else 0]))
    print(sort([(1,1), (2,2), (3,3), (5,5), (4,4)]))

def parsepts(pts):
    sortpts(pts)
    
parsepts([])
    