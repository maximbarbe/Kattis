n, m = map(int, input().split(" "))
nums = [i for i in range(1, n + 1)]
moves = []
for i in range(m):
    moves.append(int(input()) - 1)
res = [0 for i in range(len(nums))]
for i in range(len(nums)):
    pos = i
    for move in moves:
        if move == pos:
            pos += 1
        elif move == pos - 1:
            pos -= 1
    res[pos] = nums[i]
for num in res:
    print(num)
