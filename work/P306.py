def mex(s):
    i = 0
    while i in s: i+=1
    return i
L = 200
bf = [0,0]
for i in range(2, L+1):
    s = set()
    for k in range(i-1):
        s.add(bf[i-k-2] ^ bf[k])
    print(s)
    bf.append(mex(s))
#print(sum(1 if i > 0 else 0 for i in bf))
print(bf)
x = 0
