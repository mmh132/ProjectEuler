def isb(n):
    n = list(str(n))
    srt = sorted(n)
    if n == srt or n == srt[::-1]:
        return False
    return True

b, n = 0, 0
for i in range(1, 10**8):
    if isb(i): 
        b += 1
    else: 
        n += 1
    if n * 99 == b: 
        print(i)
        break