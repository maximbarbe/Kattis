from collections import defaultdict

n = int(input())
nums = defaultdict(lambda:0)
for i in range(n):
    item, quant = input().split()
    nums[item] += int(quant)
for key, item in nums.items():
    if item%64 == 0:
        print(key, item//64)
    else:
        print(key, item//64 + 1)