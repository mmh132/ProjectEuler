PL, BL = 10, 1000

def ds(n):
    if n == 0: return 0
    return n%10 + ds(n//10)

valid = set()

for b in range(2, BL):
    for e in range(2, PL):
        if ds(b**e) == b:
            valid.add(b**e)

print(sorted(list(valid))[29])
