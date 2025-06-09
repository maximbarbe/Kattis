n = int(input())
nums = [*map(int, input().split(" "))]
nums.sort()
i = 0
res = []

while i <= len(nums) - 1:
    group = [nums[i]]
    for j in range(i + 1, len(nums)):
        if nums[j] - group[-1] == 1:
            group.append(nums[j])
        else: 
            i = j
            res.append(group)
            break
    else:
        res.append(group)
        break
    
    
    
res_array = []
for i in range(len(res)):
    if len(res[i]) > 2:
        res_array.append(f"{res[i][0]}-{res[i][-1]}")
    elif len(res[i]) == 2:
        res_array.append(str(res[i][0]))
        res_array.append(str(res[i][1]))
    else:
        res_array.append(str(res[i][0]))
print(" ".join(res_array))