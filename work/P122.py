#you nerd how did you think of the prime thing and the recursion but not an iterative stop being so stupid
nums = list(range(201))
for i in range(len(nums)):nums[i] = -1
nums[0] = 0
nums[1] = 0
for i in range(8):
    nums[2**i] = i
nums[1] = 0
print(nums)
ptr = 0
best = 100
while ptr<len(nums):
    if nums[ptr]!= -1: 
        ptr+=1
    else:
        for i in range(1,int(ptr/2)+1):
            if nums[i] + nums[ptr-i] < best:
                best = nums[i] + nums[ptr-i]
        nums[ptr] = best + 1
    best = 100000
print(nums)
print(nums[15])
print()
#fix to build set of nums made in each, intersection has all nums to choose from, if inside intersection, has two numbers that add to n, num of steps+1



