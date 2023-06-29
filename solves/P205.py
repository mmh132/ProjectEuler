sid4, sid6 = [0]*37,[0]*37
def recrolldie4(sides, numrolled,total):
    if numrolled == 0: sid4[total]+=1;return
    for i in range(1,sides+1): recrolldie4(sides, numrolled-1, total+i)
def recrolldie6(sides, numrolled,total):
    if numrolled == 0: sid6[total]+=1;return
    for i in range(1,sides+1): recrolldie6(sides, numrolled-1, total+i)
recrolldie6(6,6,0);recrolldie4(4,9,0)
probability = 0
for i in range(len(sid6)):
    if sid6[i] != 0: probability+=(sid6[i]/sum(sid6))*(sum(sid4[(i+1):])/sum(sid4))
print(round(probability,7))