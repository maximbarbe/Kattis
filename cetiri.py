nums = [*map(int, input().split(" "))]
nums.sort()
if nums[1] - nums[0] == nums[2] - nums[1]:
    if nums[2] + (nums[2] - nums[1]) > 100:
        print(nums[0] - (nums[1] - nums[0]))
        exit()
    else:
        print(nums[2] + (nums[2] - nums[1]))
else:
    if nums[2] - nums[1] > nums[1] - nums[0]:
        print(nums[1] + (nums[1] - nums[0]))
    else:
        print(nums[0] + (nums[2] - nums[1]))