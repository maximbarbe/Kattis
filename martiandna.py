from collections import defaultdict
min_length = 200001
n, k, r = map(int, input().split(" "))
needed = [0 for i in range(k)]
non_zero = 0
nums = [*map(int, input().split(" "))]
for i in range(r):
    idx, amount = map(int, input().split(" "))
    if amount != 0:
        non_zero += 1
    needed[idx] = amount
    
start, cur = 0, -1
while cur != len(nums):
    if non_zero == 0:
        if (cur) - start + 1 < min_length:
            min_length = (cur)-start + 1
        needed[nums[start]] += 1
        
        if needed[nums[start]] > 0:
            non_zero += 1
        start += 1
    else:
        cur += 1
        if (cur == len(nums)):
            break
        needed[nums[cur]] -= 1
        if needed[nums[cur]] == 0:
            non_zero -= 1
        
        
if min_length == 200001:
    print("impossible")
else:
    print(min_length)