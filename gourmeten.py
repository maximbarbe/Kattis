from sys import stdin
from math import factorial

n = int(input())
m = int(input())
nums = []
res = 0

def backtrack(time_left, nums, starting_idx, num):
    global res
    if time_left < 0:
        return
    elif time_left == 0:
        temp = factorial(sum(num))
        for i in range(len(num)):
            temp //= factorial(num[i])
        res += temp
        return
    else:
        for i in range(starting_idx, len(nums)):
            num[i] += 1
            backtrack(time_left - nums[i], nums, i, num)
            num[i] -= 1
for i in range(m):
    nums.append(int(input()))
backtrack(n, nums, 0, [0 for i in range(len(nums))])
print(res)