from math import sqrt as sqt
from math import floor as flr
cap = 2*10**9
squares = []
for i in range(1,flr(sqt(cap))+1): squares.append(i**2)
reached = list()
sub, base = 0,0
while sub < len(squares) and squares[sub] + 7*squares[0] < cap:
    while squares[sub] + 7*squares[base] < cap:
        reached.append(squares[sub] + 7*squares[base])
        base+=1
    base = 0
    sub+=1
reached = [*set(reached)]
print(len(reached))
        
