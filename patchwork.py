def apply_patch(grid, x, y, patch):
    for i in range(min(len(patch), len(grid) - x)):
        for j in range(min(len(patch[i]), len(grid[i]) - y)):
            grid[x+i][y + j] = patch[i][j]
    return



R, C = map(int, input().split(" "))
res = [["." for i in range(C)] for j in range(R)]
patches = []
n = int(input())
for i in range(n):
    row, col = map(int, input().split(" "))
    patch = []
    for j in range(row):
        patch.append(input())
    patches.append(patch)

n = int(input())
for i in range(n):
    q, t, p = map(int, input().split(" "))
    p -= 1
    apply_patch(res, q, t, patches[p])

for row in res:
    print("".join(row))