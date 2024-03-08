from copy import deepcopy as dc

def amoves(x, y):
    if x < 29: yield (x+1, y)
    if x > 0: yield (x-1, y)
    if y < 29: yield (x, y+1)
    if y > 0: yield (x, y-1)

z = [0]*30
grid = [z.copy() for _ in range(30)]

rv = dc(grid)
for i in range(900):
    rv[i//30][i%30] = 1
for i in range(900):
    old, new = dc(grid), dc(grid)
    old[i//30][i%30] = 1
    for _ in range(50):
        for j in range(900):
            x, y = j//30, j%30
            m = [z for z in amoves(x, y)]
            for move in m:
                new[move[0]][move[1]] += old[x][y]/len(m)
        old, new = dc(grid), dc(grid)
    for j in range(900):
        rv[j//30][j%30] *= (1 - old[j//30][j%30])

print(sum(sum(i) for i in rv))
    
