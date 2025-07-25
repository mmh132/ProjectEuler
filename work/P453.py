from math import comb

def ap(x, y): 
    return comb((x+1)*(y+1), 2) * comb((x+1)*(y+1) - 2, 2) * 2

print(ap(2,2))