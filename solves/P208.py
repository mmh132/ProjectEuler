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

# @cache
# def dp(s, p):
#     if s[0] == MM:
#         l1 = s[1]
#         for i in range(1, 6):
#             if s[i] != l1:
#                 return 0
#         r1 = s[6]
#         for i in range(6, 11):
#             if s[i] != r1:
#                 return 0
#         return 1
#     s = list(s)
#     s[0] += 1
#     m1 = transitions[p][0]
#     m2 = transitions[p][1]
#     rv = 0
#     s[m1] += 1
#     rv += dp(tuple(s), m1)
#     s[m1] -= 1
#     s[m2] += 1
#     rv += dp(tuple(s), m2)
#     return rv

# tp = 0 
# for i in range(1, 11):
#     if i != 1 and i != 6: continue
#     tp += dp(tuple([1] + [0]*(i-1) + [1] + [0]*(10-i)), i)
# print(tp)

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

