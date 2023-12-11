#we just label cards with numbers. suite is n//13, number is n%13
from itertools import combinations
deck = set(range(52))
rv = 0
for i in combinations(deck, 5):
    for k in combinations(set(i), 4):
        x = list(k)
        if sorted([p//13 for p in x]) == [0,1,2,3] and len(set([p%13 for p in x])) == 4:
            rv += 1
            break
print(rv)
