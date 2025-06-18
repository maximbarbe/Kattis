grid = [0, 0, 0, 0, 0]
for i in range(5):
    scores = list(map(lambda x:int(x), input().split(" ")))
    grid[i] = sum(scores)

res = 0
max_index = 0
for i in range(5):
    if grid[i] > res:
        res = grid[i]
        max_index = i + 1
print(str(max_index) + " " + str(res))