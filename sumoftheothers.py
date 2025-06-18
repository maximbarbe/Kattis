import sys
for line in sys.stdin:
    nums = [*map(int, line.rstrip().split(" "))]
    sum_n = sum(nums[1:])
    i = 0 
    if sum_n == nums[i]:
        print(nums[i])
    else:
        i += 1
        while i != len(nums):
            sum_n += nums[i - 1]
            sum_n -= nums[i]
            if sum_n == nums[i]:
                print(nums[i])
                break
            
            
            
            i += 1