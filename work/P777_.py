from math import pi, cos, ceil

def d(a, b):
    rv = 0
    pts = set()
    
    #case 1 
    for n in range(1, 2*a):
        for m in range(min((2*a*b - n*b)//a, n*b//a)):
            t1 = n/a + m/b < 2
            t2 = n/a - m/b > 0
            if 0 < n/a - m/b < n/a + m/b < 2:
                if abs(cos(a*t1) - cos(a*t2)) < 0.001 and abs(cos(b*(t1 - pi/10)) - cos(b*(t2 - pi/10))) < 0.001:
                    rv += cos(a*t1)**2 + cos(b*(t1 - pi/10))**2
                    pts.add((cos(a*t1), cos(b*(t1 - pi/10))))
    
    #case 2
    for m in range(ceil(19*b/10)):
        for n in range(min(ceil(19*a*b/10)-a*m, ceil((-b/10-m*a)/b))):
            t1 = n/a + m/b + 1/10< 2
            t2 =  -n/a + m/b + 1/10 > 0
            if 0 < -n/a + m/b + 1/10 < n/a + m/b + 1/10 < 2:
                if abs(cos(a*t1) - cos(a*t2)) < 0.001 and abs(cos(b*(t1 - pi/10)) - cos(b*(t2 - pi/10))) < 0.001:
                    rv += cos(a*t1)**2 + cos(b*(t1 - pi/10))**2
                    pts.add((cos(a*t1), cos(b*(t1 - pi/10))))
    
    return rv, pts

print(d(2, 5))


