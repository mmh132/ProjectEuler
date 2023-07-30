#working theory, cuts make it 

def bfF(x,y):
    rv = 0
    things = set()
    for i in range(1, max(x, y)):
        if x%i == 0 and y%(i+1) == 0:
            rv += 1 if x//i > 1 or y//(i+1) > 1 else 0
            things.add(tuple(sorted((x*(i+1)//i, y*i//(i+1)))))
        if y%i == 0 and x%(i+1) == 0:
            rv += 1 if y//i > 1 or x//(i+1) > 1 else 0
            things.add(tuple(sorted((y*(i+1)//i, x*i//(i+1)))))
    print(x,y,things)
    return len(things) - 1 if (x,y) in things else 0

def bfG(n):
    rv = 0
    for x in range(1, n+1):
        for y in range(x, n+1):
            rv += bfF(x,y)
    return rv

print(bfG(10))