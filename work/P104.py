import sys
sys.set_int_max_str_digits(0)
def ispandigitalend(n):
    stor = sorted(str(n)[-9:])
    if stor == ['1','2','3','4','5','6','7','8','9']: return True
    return False
def ispandigitalstart(n):
    stor = sorted(str(n)[:9])
    if stor == ['1','2','3','4','5','6','7','8','9']: return True
    return False
f1 = 1
f2 = 1
curr = 3
fcurr = f1+f2
while ispandigitalend(fcurr)!= True or ispandigitalstart(fcurr)!= True:
    f1 = f2
    f2 = fcurr
    fcurr = f1+f2
    curr+=1
    print(curr)