class rand:
    def __init__(self):
        self.a = 290797
    def __next__(self):
        self.a = (self.a * self.a) % 50515093
        return self.a 
def eval(x):
    rv = 1
    for idx, i in enumerate(x):
        rv *= pow(i, idx+1)
    return rv
out = 0
rando = rand()
iters = 300000   
for size in range(2, 16):
    xs = [1]*size
    d = 0.01
    unc = 0
    for i in range(iters):
        if unc > 100: unc = 0; d/=10
        id1 = next(rando) % size
        id2 = next(rando) % size
        if id1 == id2: continue
        curr = eval(xs)
        xs[id1] += d
        xs[id2] -= d
        new = eval(xs)
        if new < curr:
            xs[id1] -= d
            xs[id2] += d
            unc += 1
        else:
            unc = 0
    print(d)
    out += int(eval(xs))
print(out)

