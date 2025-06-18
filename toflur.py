n = int(input())
res = 0
nums = [*map(int, input().split(" "))]
nums.sort()
for i in range(len(nums) - 1):
    res += (nums[i] - nums[i + 1])**2
print(res)