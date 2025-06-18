from math import isqrt

n = int(input())
for i in range(n):
    string = input()
    length = len(string)
    i = 0
    while (length + i) != isqrt(length + i) ** 2:
        i += 1
    string = string + "*" * i
    root = isqrt(len(string))
    grid = []
    for i in range(root):
        grid.append([char for char in string[i*root:i*root + root]])
    new_grid = [[None for i in range(root)] for j in range(root)]
    for i in range(root):
        for j in range(root):
            new_grid[j][root - i - 1] = grid[i][j]
    res = ""
    for i in range(root):
        for j in range(root):
            if new_grid[i][j] != "*":
                res += new_grid[i][j]
    print(res)