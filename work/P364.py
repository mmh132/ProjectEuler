# def dp(l, r, s):
#     rv = 0
#     for i in range(1 if l else 0, s-1 if r else s):
#         rv += dp(l, True, i-1)*dp(True, r, s-i)
#     return rv if rv>0 else 1
# print(dp(True, True, 1))

#this is dumb, you cant split into subproblems this way