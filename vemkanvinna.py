def wins(grid):
    for i in range(len(grid)):
        cur = set(grid[i])
        if len(cur) == 1:
            if "X" in cur:
                return 1
            elif "O" in cur:
                return 2
    for i in range(len(grid)):
        if grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] == "X":
                return 1
            elif grid[0][i] == "O":
                return 2
    if grid[0][0] == grid[1][1] == grid[2][2]:
        if grid[0][0] == "X":
            return 1
        elif grid[0][0] == "O":
            return 2
    if grid[2][0] == grid[1][1] == grid[0][2]:
        if grid[2][0] == "X":
            return 1
        elif grid[2][0] == "O":
            return 2
    return 0


abdullah = johan = False

def dfs(turn, grid):
    global abdullah,johan
    res = wins(grid)
    if res == 1:
        johan = True
        return
    elif res == 2:
        abdullah = True
        return
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "_":
                grid[i][j] = turn
                dfs("O" if turn == "X" else "X", grid)
                grid[i][j] = "_"

    

            
grid = []
a,j = 0, 0
for i in range(3):
    grid.append(input().split())
    for char in grid[-1]:
        if char == "X":
            j += 1
        elif char == "O":
            a += 1
if a == j:
    
    dfs("X", grid)
else:
    dfs("O", grid)
if abdullah and johan:
    print("Abdullah och Johan kan vinna")
elif abdullah:
    print('Abdullah kan vinna')
elif johan:
    print("Johan kan vinna")
else:
    print("ingen kan vinna")