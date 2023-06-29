def check(start, compare):
    if sorted(str(start)) == sorted(str(compare)):
        return True
    return False

counter = 1
found = False
while found == False:
    if check(counter, 2*counter) == True:
        if check(counter, 3*counter) == True:
            if check(counter, 4*counter) == True:
                if check(counter, 5*counter) == True:
                    if check(counter, 6*counter) == True:
                        found == True
                        print(counter)
                        break
    counter +=1