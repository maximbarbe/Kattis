n = int(input())
nums = []
for i in range(n):
    nums.append(input())
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])