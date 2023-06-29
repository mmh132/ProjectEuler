path = [[1,7], [2,8], [3,9], [4,5], [0,6], [6,3], [7,4], [8,0], [9,1], [5, 2]]
tv = [0]*10
def recrun(c, v, d):
    if d == 25:
        if v[0] == v[1] == v[2] == v[3] == v[4]:
            if v[5] == v[6] == v[7] == v[8] == v[9]:
                return 1
        return 0
    rv = 0
    for n in path[c]:
        v[n] += 1
        rv += recrun(n, v, d+1)
        v[n] -= 1
    return rv

print(recrun(8, tv, 0))
