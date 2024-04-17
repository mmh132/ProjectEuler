from functools import cache

N = 13
#let l be the last pile you took from, r be the number of perfec

def dp(n_0, n_1, n_2, n_3, l, r):
    n_4 = N - (n_0 + n_1 + n_2 + n_3)
    if n_4 == N: 
        return r
    cl = 13 * 4 - (n_1 * 1 + n_2 * 2 + n_3 * 3 + n_4 * 4)

    rv = 0
    if n_0 > 0: 
        if l == 0:
            rv += dp(n_0 - 1, n_1 + 1, n_2, n_3, l, r)
        else:

            pass
    pass

#this fails, you have to store "imperfect ranks with 2, 3, 4 placed"

