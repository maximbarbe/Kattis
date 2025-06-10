n = int(input())
for i in range(n):
    nums = [*map(lambda el: int(el) - 1, input().split())]
    print(sum(nums[1:]) + 1)