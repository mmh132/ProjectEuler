# def bm(s):
#     c, oldc = [], []
#     f = -1
#     for i in range(len(s)):
#         delta = s[i]
#         for j in range(1, len(c) + 1):
#             delta -= c[j-1] * s[i-j]
#         if delta == 0: 
#             continue
#         if f == -1:
#             c = [0] * (i + 1)
#             f = i
#         else:
#             d = oldc.copy()
#             for _ in range(len(d)):
#                 d[_] *= -1
#             d = [1] + d
#             df1 = 0
#             for j in range(1, len(d) + 1):
#                 df1 += d[j-1] * s[f+1-j]
#             assert df1 != 0
#             coef = delta//df1
#             for _ in range(len(d)):
#                 d[_] *= coef
#             d = [0]*(i-f-1) + d
#             temp = c.copy()
#             while len(c) < len(d):
#                 c.append(0)
#             for j in range(len(d)):
#                 c[j] += d[j]
#             if i - len(temp) > f - len(oldc):
#                 oldc = temp.copy()
#                 f = i
#             print(c)
#     return c

def berlekamp_massey(arr):
    # 返り値は数列の後ろに掛けるやつが前（伝われ）
    n = len(arr)
    bs = [1]
    cs = [1]
    y = 1
    for ed in range(1, n+1):
        len_cs, len_bs = len(cs), len(bs)
        x = sum(c * arr[ed-len_cs+i] for i, c in enumerate(cs)) 
        bs.append(0)
        len_bs += 1
        if x == 0:
            continue
        freq = x / y
        if len_cs < len_bs:
            tmp = cs[:]
            cs = [0] * (len_bs - len_cs) + cs
            cs = [(c-b*freq) for c, b in zip(cs, bs)]
            bs = tmp
            y = x
        else:
            for i, b in enumerate(reversed(bs), 1):
                cs[-i] = (cs[-i] - freq * b) 
        for i in range(len_cs):
            cs[i] = round(cs[i], 10)
    return [-c  for c in cs[-2::-1]]

print(berlekamp_massey([]))