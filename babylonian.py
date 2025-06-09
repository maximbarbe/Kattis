n = int(input())
for i in range(n):
    nums = input().split(",")
    res = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != '':
            res += int(nums[i]) * 60**(len(nums) -1 - i)
    print(res)