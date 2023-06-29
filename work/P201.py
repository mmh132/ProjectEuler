from copy import deepcopy as dc
import math
inset = [x**2 for x in range(1,101)]
maxnum = sum(inset[50:]) + 1
print(maxnum)
l = [0]*maxnum
coeffs = []
for i in range(51): coeffs.append(dc(l))
coeffs[0][0] = 1
for i in inset:
    print(math.sqrt(i))
    for setsize in range(len(coeffs)-2,-1,-1):
        for index in range(len(coeffs[setsize])):
            if coeffs[setsize][index] != 0:
                coeffs[setsize+1][index+i] += coeffs[setsize][index]
s = 0
for i in range(len(coeffs[50])): 
    if coeffs[50][i] == 1: s += i
print(s)