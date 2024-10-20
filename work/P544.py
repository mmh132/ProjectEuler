N, M = 9, 10

# #build masks for row configs, based on relations between colors
# def CC(len):
#     if len == 1: return [[1]]
#     rv = []
#     for i in CC(len-1):
#         for k in range(1, max(i) + 2):
#             if k != i[-1]:
#                 rv.append(i[:] + [k])
#     return rv

# print(len(CC(9)))

#row should be canonical form 
def dp(row, idx, c, l):
    if idx == N - 1: l += 1
    ill = 1 if row[-1] == row[0] else 2
    vals = set(row[1:-1])
    for i in vals: 
        dp(row[1:] + [i], (idx + 1) % N, c, l)
    