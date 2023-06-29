def p(k,n):
    p0 = pow((n-1)/n, k)
    p1 = (k/1000000) * pow((n-1)/n, k-1)
    p2 = (k/1000000) * ((k)/1000000) * pow((n-1)/n, k-2)
    return 1-(p0+p1+p2)*n
print(p(3,7))