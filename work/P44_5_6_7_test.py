def sectest(n):
    tot = 0
    for a in range(1, n):
        for b in range(0, n):
            good_exit = True
            for x in range(n):
                t = (a*x + b) % n
                if (a*t) % n != a*x % n:
                    good_exit = False
            if good_exit == True:
                #print(a, b, n)
                tot += 1
    # print("did a total of %d" %(tot))
    return tot

def test(n):
    tot = 0
    for a in range(1, n):
        for b in range(n):
            if a*a % n == a:
                if a*b % n == 0:
                    tot += 1

    return tot



print(sum(test(i) for i in range(1, 201)))