n, m = map(int, input().split())
positions = [*map(int, input().split())]
trees = [*map(int, input().split())]

positions.sort()
trees.sort()
claimed = [False for i in range(m)]
res = 0
for val in positions:
    smallest_dist = 1000001
    tree_idx = 0
    for i in range(len(trees)):
        if abs(val - trees[i]) < smallest_dist:
            smallest_dist = abs(val - trees[i])
            tree_idx = i
    if claimed[tree_idx]:
        res += 1
    else:
        claimed[tree_idx] = True
print(res)
            