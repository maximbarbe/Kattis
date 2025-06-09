
def get_status(grid):
    for i in range(3):
        chars = set(grid[i])
        if len(chars)== 1 and "." not in chars:
            return chars.pop()
    for i in range(3):
        col = [grid[j][i] for j in range(3)]
        chars = set(col)
        if len(chars)== 1 and "." not in chars:
            return chars.pop()
    if grid[0][0] == grid[1][1] == grid[2][2] != ".":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != ".":
        return grid[1][1]
    
    for i in range(3):
        for j in range(3):
            if grid[i][j] == ".":
                return "In progress"
    else:
        return "Cat's"
n = int(input())
for i in range(n):
    grid = [["." for i in range(3)] for j in range(3)]
    state = bin(int(input(), 8))[2:].zfill(19)[::-1]
    for i in range(9, 18):
        if state[i-9] == "1":
            posi = (i - 9)//3
            posj = (i-9)%3
            if state[i] == "1":
                grid[posi][posj] = "X"
            else:
                grid[posi][posj] = "O"
    c = get_status(grid)
    if c in "XO":
        print(f"{c} wins")
    else:
        print(c)