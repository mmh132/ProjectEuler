import math
from decimal import *
from decimal import Decimal
getcontext().prec = 100
def func(y):
    y = Decimal(y)
    v = Decimal(1+math.sqrt(2*y**2 - 2*y + 1))/Decimal(2)
    return v == int(v)
def check(x,y):
    return Decimal(1)/Decimal(2) == Decimal(x*(x-1))/Decimal(y*(y-1))
found = 0
y = 10**12+1
while found<1:
    y+=1
    if func(y) == True: 
        if check((1+math.sqrt(2*y**2 - 2*y + 1))/2, y):
            print([(1+math.sqrt(2*y**2 - 2*y + 1))/2, y])
            found +=1


    