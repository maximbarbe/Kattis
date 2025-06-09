import sys
from collections import defaultdict

grid = []
positions = defaultdict(lambda:0)
row = 0
for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        cur_idx = 0
        line_length = len(grid[0])
        for i in range(len(grid) - 1, -1, -1):
            grid[i] = "." * cur_idx + "*"*positions[i] + "." * (len(grid[i]) - cur_idx - positions[i])
            cur_idx += positions[i]
        for rows in grid:
            print(rows)
        print()
        grid = []
        positions = defaultdict(lambda:0)
        row = 0

    else:
        positions[row] = line.count("*")
        grid.append([char for char in line])
        row += 1
else:
    cur_idx = 0
    line_length = len(grid[0])
    for i in range(len(grid) - 1, -1, -1):
        grid[i] = "." * cur_idx + "*"*positions[i] + "." * (len(grid[i]) - cur_idx - positions[i])
        cur_idx += positions[i]
    for rows in grid:
        print(rows)
    