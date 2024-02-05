def tester(n):
    rv = 0
    for i in range(1, n+1):
        if n%i == 0:
            a = i
            b = n//i
            if a == 1 or b == 1 or a == 2 or b == 2:
                continue
            found = False
            for j in range(2, min(a,b)+1):
                if a%j == b%(j+1) == 0 or b%j == a%(j+1) == 0:
                    found = True
                    print(a, b, j)
                    break
            if not found:
                print(a, b)
                rv += 1
    return rv

print(tester(1320))
