from functools import cache

transitions = {
    1: (10, 2),
    2: (9, 3),
    3: (8, 4),
    4: (7, 5),
    5: (6, 1),
    6: (5, 7),
    7: (4, 8),
    8: (3, 9),
    9: (2, 10),
    10: (1, 6)
}

MM = 70

@cache
def dp(s, p):
    s = list(s)
    h = False
    for i in s:
        if i != 0: h = True
        if i < 0: return 0
    if not h: return 1
    m1 = transitions[p][0]
    m2 = transitions[p][1]
    rv = 0
    s[m1] -= 1
    rv += dp(tuple(s), m1)
    s[m1] += 1
    s[m2] -= 1
    rv += dp(tuple(s), m2)
    return rv

tp = 0 
for i in range(MM//5 + 1):
    print(tuple([0] + [i]*5 + [MM//5 - i]*5))
    tp += dp(tuple([0] + [i]*5 + [MM//5 - i]*5), 10)
print(tp)

