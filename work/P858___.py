from math import lcm
def f(set):
    d = {1:1}
    for i in set:
        t = d.copy()
        for key in d:
            if lcm(i, key) in t:
                t[lcm(i, key)] += d[key]
            else:
                t[lcm(i, key)] = d[key]
        d = t.copy()
    print(d)
    print(sum(i*d[i] for i in d))

print(f([1,2,1,4,1,2]))