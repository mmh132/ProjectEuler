#we just label cards with numbers. suite is n//13, number is n%13
from itertools import combinations
def bf(n):
    deck = set(range(52))
    rv = 0
    for i in combinations(deck, n):
        for k in combinations(set(i), 4):
            x = list(k)
            if sorted([p//13 for p in x]) == [0,1,2,3] and len(set([p%13 for p in x])) == 4:
                rv += 1
                break
    print(rv)

def valid(m1, m2, m3, m4):
    s = set()
    for i in range(13):
        for j in range(i, 13):
            if ((m1 >> i)&1 and (m2 >> j)&1) or ((m1 >> j)&1 and (m2 >> i)&1):
                s.add((1 << i) + (1 << j))

    for i in range(13):
        for j in range(i, 13):
            if ((m3 >> i)&1 and (m4 >> j)&1) or ((m3 >> j)&1 and (m4 >> i)&1):
                y = (1 << i) + (1 << j)
                for x in s:
                    if x + y == x ^ y:
                        return True
                    
    return False

def dp(m1, m2, m3, m4, l):
    for i in range(1, 1 << 4):
        dp(m1 ^ (i >> 0)&1)



