def f(n, size):
    set1 = set(n)
    for i in range(len(n)):
        n[i]*=2
    set2 = set(n)
    for i in range(len(n)):
        n[i]/=2
        n[i]*=3
        n[i] = int(n[i])
    set3 = set(n)
    if set1.intersection(set2,set3) != set():
        print(set1.intersection(set2,set3))
    else: 
        newset = set1.union(set2,set3)
        print(len(list(newset.intersection(set(list(range(1,size+1)))))))
        print(newset.intersection(set(list(range(1,size)))))
        print(set(list(range(1,size))).difference(newset))
f([1,4,5,7,9,11,13,16,17,19,20,23,25,28,29,31,35,36,37,41,43,44,45,47,49,50], 50)

def banana(n):
    set1 = set(n)
    for i in range(len(n)):
        n[i]*=2
    set2 = set(n)
    for i in range(len(n)):
        n[i]/=2
        n[i]*=3
        n[i] = int(n[i])
    set3 = set(n)
    print(set1.difference(set2, set3))
i = 6
thing = []
while i < 100:
    thing.append(i)
    i += 6
print(thing)
banana(thing)