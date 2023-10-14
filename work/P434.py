from math import comb


def f(w,h):
    rv = 0
    for p in range(w*h+1):
        for r in range(h+1):
            for c in range(w+1):
                m = comb(w*h, p)*comb(h,r)*comb(w,c)
                
