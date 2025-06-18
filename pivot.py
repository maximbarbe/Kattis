import heapq
from math import inf

n = int(input())
right = set()
left = set()
nums = [*map(int, input().split(" "))]
minimums = [0 for i in range(len(nums))]
minimums[-1] = inf
maximums = [0 for i in range(len(nums))]
maximums[0] = -inf
for i in range(1, len(nums)):
    maximums[i] = max(nums[i-1], maximums[i - 1])
for i in range(len(nums) - 2, -1, -1):
    minimums[i] = min(minimums[i + 1], nums[i + 1])
    
res = 0
for i in range(len(nums)):
    if maximums[i] <= nums[i] < minimums[i]:
        res += 1
print(res)