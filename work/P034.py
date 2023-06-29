factorials = [1]
while len(factorials) < 10: 
    factorials.append(factorials[-1]*(len(factorials)))
def isfac(n):
    tot = 0
    for i in list(str(n)):
        tot += factorials[int(i)]
        if tot>n: return False
    if tot == n: return True
tot = 0
for i in range(1,5000000):
    if isfac(i):
        tot+=i
        print(str(i) + " added, produced " + str(tot))
