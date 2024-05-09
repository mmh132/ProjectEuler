from itertools import chain, combinations
from functools import cache

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

def moves(pile, deck):
    poss = []
    for i in deck:
        for j in pile:
            poss.append((i, j))
    for i, j in poss:
        if j < i:
            pile.remove(j)
            pile.add(i)
            deck.remove(i)
            yield tuple(sorted(list(pile))), tuple(sorted(list(deck)))
            pile.add(j)
            pile.remove(i)
            deck.add(i)
    

def g(pile, deck):
    if deck == set(): return 0
    return mex([g(set(i), set(j)) for i, j in moves(pile, deck)])

def ss(s):
    xs = list(s)
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))


def bf(n, s):
    def xormul(a, b):
        rv = [0] * 8
        for idx, i in enumerate(a):
            for jdx, j in enumerate(b):
                rv[idx^jdx] += i*j
        return rv
    
    vals = [0] * n
    for i in ss(range(1, n + 1)):
        ni = set([x for x in i])
        j = set(range(1, n + 1)) - ni
        vals[g(ni, j)] += 1

    return vals


N = 6
for i in ss(range(1, N + 1)):
    ni = set([x for x in i])
    j = set(range(1, N + 1)) - ni
    st = ""
    for i in range(1, N + 1):
        if i in ni:
            st += "L"
        else:
            st += "R"
    #print(ni, j, g(ni, j))

for i in range(2, 15):
    x= bf(i, 1)
    print(x, " len ", len(x))

#rule is number in right greater than least in left
    #fails for 1,2 - 3, 4, 5 -> 1
