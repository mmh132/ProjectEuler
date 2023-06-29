

def bm(seq):
    c, oldc = [], []
    f = -1
    for i in range(len(seq)):
        delta = seq[i]
        for k in range(1,len(c)):
            delta -= c[k-1] * seq[i-k]
        if delta == 0:
            continue
        if f == -1:
            c.append(0)
            f = i
        else: 
            
