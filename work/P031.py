binngbon = [1,2,5,10,20,50,100,200]
def coinpartitions(sum,max):
    if sum == 0 or max == 0:return 1
    rv,ctr = 0,0
    while ctr*binngbon[max] <=sum: rv+= coinpartitions(sum-ctr*binngbon[max], max-1);ctr+=1
    return rv
print(coinpartitions(200,7))


