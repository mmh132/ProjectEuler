def g(pl):
    pl = sorted(pl)
    while pl[-1] == 0: pl.pop(-1)
    if len(pl) == 1: return 2**(pl[0]-1)
    if len(pl) == 0: return 1