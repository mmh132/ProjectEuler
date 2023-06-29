def avg(n):
    return sum(n)/len(n)

def tester(m):
    found = []
    def smallcase(n, emp):
        if n<0: return 
        if n == 0: found.append(emp)
        for i in range(2,4):
            smallcase(n-i, emp+i-1)
    smallcase(m,0)
    print(found)
    return avg(found)/m
print(tester(6))


