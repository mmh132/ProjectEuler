

def bm(s):
    c = []
    oldc = []
    f = -1
    for i in range(len(s)):
        print(c, oldc)
        si = s[i]
        delta = si - sum([c[j-1]*s[i-j] for j in range(1, len(c)+1)])
        print(si, delta)
        if delta == 0: continue
        if f == -1:
            c = [1]*(i+1)
            f = i
            continue
        d = [1] + [-x for x in oldc]
        scale = delta / sum([d[j-1]*s[f+1-j] for j in range(1, len(d)+1)])
        for i in range(len(d)): 
            d[i]*=scale
        df = [0]*(i-f-1) + d.copy()
        temp = c.copy()
        for i in range(len(df)):
            if i < len(c):
                df[i] += c[i]
        c = df.copy()
        if i-len(temp) > f-len(oldc):
            oldc = temp.copy()
            f = i
    return [int(i) for i in c]

print(bm([1,2,4,8,13,20,28,215,757,2186]))

        
# c is recurrence
# s is initial sequence
# k is term
def lr(c, s, k):
    assert len(c) <= len(s)

    

  

