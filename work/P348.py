def ispal(n): return str(n) == str(n)[::-1]
d = dict()
for sq in range(1, 10**6):
    for cb in range(1,10**4):
        a = sq**2 + cb**3
        if ispal(a):
            if a in d: 
                d[a]+=1
            else: 
                d[a] = 1
s = 0
for a in d: 
    if d[a] >= 4: 
        s += a
        print(a)
