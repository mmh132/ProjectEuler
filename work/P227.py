def f(d, p, s):
    if d > 5: d = 10-d
    if d < 0: d = abs(d)
    if d == 0: return s*p
    if p < 10**-5: return 0
    rv = 0
    rv += f(d, p*0.5, s+1)
    rv += f(d-1, p*(2/9), s+1)
    rv += f(d+1, p*(2/9), s+1)
    rv += f(d-2, p*(1/36), s+1)
    rv += f(d+2, p*(1/36), s+1)
    return rv
print(f(50, 1, 0))