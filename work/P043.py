tot = [0]
def reverse(s):
    if len(s) == 0: return s
    return reverse(s[1:]) + s[0]
def recbuild(cur, bank):
    if len(bank) == 0 and cur[-1] != "0": tot[0]+=int(reverse(cur))
    if len(cur) == 3:
        if int(reverse(cur[-3:])) % 17 != 0: return
    if len(cur) == 4: 
        if int(reverse(cur[-3:])) % 13 != 0:return
    if len(cur) == 5: 
        if int(reverse(cur[-3:])) % 11 != 0:return
    if len(cur) == 6: 
        if int(reverse(cur[-3:])) % 7 != 0:return
    if len(cur) == 7: 
        if int(reverse(cur[-3:])) % 5 != 0:return
    if len(cur) == 8: 
        if int(reverse(cur[-3:])) % 3 != 0:return
    if len(cur) == 9: 
        if int(reverse(cur[-3:])) % 2 != 0:return
    temp = bank.copy()
    for i in temp:
        temp = bank.copy()
        temp.remove(i)
        recbuild(cur+str(i), temp)
recbuild("", list(range(0,10)))
print(tot)
