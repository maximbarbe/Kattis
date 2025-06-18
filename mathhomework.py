def backtrack(nums, total, cur, starting_idx):
    global res
    if total < 0:
        return
    if total == 0:
        res.append(tuple(cur))
    for i in range(starting_idx, len(nums)):
        cur[i] += 1
        backtrack(nums, total - nums[i], cur, i)
        cur[i] -= 1

b, d, c, l = map(int, input().split(" "))
res = []
nums= [b, d, c]
backtrack(nums, l, [0, 0, 0], 0)
res.sort(key=lambda el: (el[0], el[1], el[2]))
if res != []:
    for val in res:
        print(" ".join(map(str, val)))
else:
    print("impossible")