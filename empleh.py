grid = [[None for i in range(8)] for j in range(8)]
for i in range(len(grid)):
    
    for j in range(len(grid)):
        if i % 2 == 0 and j % 2 == 0:
            grid[i][j] = "..."
        elif i % 2 == 0 and j % 2 != 0:
            grid[i][j] = ":::"
        elif i % 2 == 1 and j % 2 == 0:
            grid[i][j] = ":::"
        else:
            grid[i][j] = "..."
white = input().split(" ")[1].split(",")
black = input().split(" ")[1].split(",")
if white[0] != '':
    for el in white:
        if len(el) == 2:
            col = ord(el[0])  - ord("a")
            row = 7 - (int(el[1]) - 1)
            grid[row][col] = grid[row][col][0] + "P" + grid[row][col][2]
        else:
            symbol = el[0]
            col = ord(el[1])  - ord("a")
            row = 7 - (int(el[2]) - 1)
            grid[row][col] = grid[row][col][0] + symbol + grid[row][col][2]
if black[0] != '':
    for el in black:
        if len(el) == 2:
            col = ord(el[0])  - ord("a")
            row = 7 - (int(el[1]) - 1)
            grid[row][col] = grid[row][col][0] + "p" + grid[row][col][2]
        else:
            symbol = el[0]
            col = ord(el[1])  - ord("a")
            row = 7 - (int(el[2]) - 1)
            grid[row][col] = grid[row][col][0] + symbol.lower() + grid[row][col][2]
for i in range(len(grid)):
    print("+---+---+---+---+---+---+---+---+")
    print("|" + "|".join(grid[i]) + "|")
print("+---+---+---+---+---+---+---+---+")