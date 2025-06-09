import sys


order = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
cur = "0"
cur_max_idx = 0
max_char = "0"
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
grid = []
indices = dict()
i = 0
for line in sys.stdin:
    
    line = line.rstrip()
    if line == "":
        cur = "0"
        idx = 0
        dir = None
        while cur != max_char:
            diff = (indices[order[idx + 1]][0] - indices[cur][0], indices[order[idx + 1]][1] - indices[cur][1])
            if diff[0] == 0:
                if diff[1] < 0:
                    dir = (0, -1)
                else:
                    dir = (0, 1)
            else:
                if diff[0] < 0:
                    dir = (-1, 0)
                    
                else:
                    dir = (1, 0)
            x, y = indices[cur]
            while (x, y) != indices[order[idx + 1]]:
                x += dir[0]
                y += dir[1]
                if dir[0] == 0:
                    if grid[x][y] == ".":
                        grid[x][y] = "-"
                    elif grid[x][y] == "|":
                        grid[x][y] = "+"
                else:
                    if grid[x][y] == ".":
                        grid[x][y] = "|"
                    elif grid[x][y] == "-":
                        grid[x][y] = "+"
            cur = order[idx + 1]
            idx += 1
        for row in grid:
            print("".join(row))
        cur = "0"
        max_char = "0"
        cur_max_idx = 0
        grid = []
        indices = dict()
        i = 0
        continue
    row = []
    for j in range(len(line)):
        if line[j] != ".":
            indices[line[j]] = (i, j)
            if order.index(line[j]) > cur_max_idx:
                cur_max_idx = order.index(line[j])
                max_char = line[j]
        row.append(line[j])
    grid.append(row)
    i += 1
else:
    cur = "0"
    idx = 0
    dir = None
    while cur != max_char:
        diff = (indices[order[idx + 1]][0] - indices[cur][0], indices[order[idx + 1]][1] - indices[cur][1])
        if diff[0] == 0:
            if diff[1] < 0:
                dir = (0, -1)
            else:
                dir = (0, 1)
        else:
            if diff[0] < 0:
                dir = (-1, 0)
                
            else:
                dir = (1, 0)
        x, y = indices[cur]
        while (x, y) != indices[order[idx + 1]]:
            x += dir[0]
            y += dir[1]
            if dir[0] == 0:
                if grid[x][y] == ".":
                    grid[x][y] = "-"
                elif grid[x][y] == "|":
                    grid[x][y] = "+"
            else:
                if grid[x][y] == ".":
                    grid[x][y] = "|"
                elif grid[x][y] == "-":
                    grid[x][y] = "+"
        cur = order[idx + 1]
        idx += 1
    for row in grid:
        print("".join(row))
    cur = "0"
    max_char = "0"
    grid = []
    indices = dict()