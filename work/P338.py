from math import isqrt
def bfF(x,y):
    out = set()
    for i in range(1, max(x,y)):
        if x%i == 0 and y%(i+1) == 0:
            new = [(x//i)*(i+1), (y//(i+1))*i]
            out.add(tuple(sorted(new)))
        if y%i == 0 and x%(i+1) == 0:
            new = [(y//i)*(i+1), (x//(i+1))*i]
            out.add(tuple(sorted(new)))
    #print(x,y,out)
    rv = len(out)
    if tuple(sorted([x,y])) in out:
        rv -= 1
    return rv

def bfFalt(x,y):
    out = list()
    for i in range(1, max(x,y)):
        if x%i == 0 and y%(i+1) == 0:
            new = [(x//i)*(i+1), (y//(i+1))*i]
            out.append(tuple(sorted(new)))
            print(i, i+1, out[-1], x)
        if y%i == 0 and x%(i+1) == 0:
            new = [(y//i)*(i+1), (x//(i+1))*i]
            out.append(tuple(sorted(new)))
            print(i, i+1, out[-1], y)
    if len(set(out)) < len(out):
        print(x,y,out)
    rv = len(out)
    if tuple(sorted([x,y])) in out:
        rv -= 1
    return rv

#check to see if it works if we only allow strictly smaller fraction for the first
#nope, counterexample is 5,6
# def bfFalt2(x,y):
#     out = set()
#     for i in range(1, max(x,y)):
#         if y%i == 0 and x%(i+1) == 0:
#             new = [(y//i)*(i+1), (x//(i+1))*i]
#             out.add(tuple(sorted(new)))
#     print(x,y,out)
#     rv = len(out)
#     if tuple(sorted([x,y])) in out:
#         rv -= 1
#     return rv

def bfG(n):
    rv = 0
    for x in range(1, n+1):
        for y in range(x, n+1):
            rv += bfF(x,y)
    return rv
x,y = 5,6
#print(bfG(10))
print(bfF(x,y))




