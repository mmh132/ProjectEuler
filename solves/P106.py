from math import comb, factorial
N = 12
rv = 0

for i in range(2**N):
    for j in range(i+1, 2**N):
        if i & j: continue
        ti, tj = i, j
        cti, ctj = 0,0
        while ti:
            cti += ti&1
            ti >>= 1
        while tj:
            ctj += tj&1
            tj >>= 1
        if cti != ctj or cti < 2:
            continue
        cbi, cbj = 0, 0
        found = 0
        for _ in range(cti):
            while not (1 << cbi) & i: cbi += 1
            while not (1 << cbj) & j: cbj += 1
            if cbi > cbj:
                found += 1
            else: 
                found -= 1
            cbi += 1
            cbj += 1
        if not abs(found) == cti:
            print(i, j)
            rv += 1

print(rv)
            

 