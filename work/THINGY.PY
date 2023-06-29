memos = {0:1, 1:1, 2:1, 3:2}
def recbuild(left):
    if left in memos: return memos[left]
    memos[left] = 1 + sum([recbuild(left-i-shift-1) for i in range(3,left+1) for shift in range(0,left-i-1)])
    return memos[left]
print(recbuild(50))