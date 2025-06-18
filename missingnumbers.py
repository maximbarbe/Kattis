n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
if nums[-1] == n:
    print("good job")
else:
    all_nums = list(set([i for i in range(1, nums[-1] + 1)]).difference(set(nums)))
    all_nums.sort()
    for i in range(len(all_nums)):
        print(all_nums[i])