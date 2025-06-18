c = 0
while True:
    c += 1
    n, m = map(int, input().split(" "))
    if n == 0 and m == 0:
        break
    grid = []
    row, col = None, None
    for i in range(m):
        string = input()
        rows = []
        for j in range(len(string)):
            if string[j] == "*":
                row, col = i, j
            rows.append(string[j])
        grid.append(rows)
    dir = None
    if col == 0:
        dir = (0, 1)
    elif col == n-1:
        dir = (0, -1)
    elif row == 0:
        dir = (1, 0)
    else:
        dir = (-1, 0)
    while grid[row][col] != "x":
        row += dir[0]
        col += dir[1]
        if grid[row][col] == "/":
            if dir == (0, 1):
                dir = (-1, 0)
            elif dir == (0, -1):
                dir = (1, 0)
            elif dir == (1, 0):
                dir = (0, -1)
            else:
                dir = (0, 1)
        elif grid[row][col] == "\\":
            if dir == (0, 1):
                dir = (1, 0)
            elif dir == (0, -1):
                dir = (-1, 0)
            elif dir == (1, 0):
                dir = (0, 1)
            else:
                dir = (0, -1)
    grid[row][col] = "&"
    print(f"HOUSE {c}")
    for row in grid:
        print("".join(row))