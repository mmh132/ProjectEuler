def crt(cg):
    m = 1
    for i in cg:
        m *= i[1]
    rv = 0
    for i in cg:
        a = i[0]
        m1 = m//i[1]
        n1 = pow(m1,-1,i[1])
        rv = (rv + a * m1 % m * n1) % m
    return rv

def G(a,b):
    #factor a,b
    