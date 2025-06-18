probs = {
    2: 1/36,
    3: 1/18,
    4: 3/36,
    5: 1/9,
    6: 5/36,
    7: 1/6,
    8: 5/36,
    9: 1/9,
    10: 3/36,
    11: 1/18,
    12: 1/36
}
n = int(input())
res = 0
nums = list(map(lambda x: int(x), input().split(" ")))
for i in range(len(nums)):
    res += probs[nums[i]]
print(res)