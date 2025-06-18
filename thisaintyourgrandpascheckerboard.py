from collections import Counter
n = int(input())
grid = []

# row check
for i in range(n):
    line = input()
    counter = Counter(line)
    if counter['W'] != counter['B']:
        print(0)
        exit()
    grid.append(line)
  
# Column check
for i in range(n):
    white = 0
    black = 0
    for j in range(n):
        if grid[j][i] == 'B':
            black += 1
        else:
            white += 1
        
        
    if white != black:
        print(0)
        exit()      
        

if n > 2:
    # row check
    for i in range(len(grid)):
        for j in range(len(grid) - 2):
            if grid[i][j] == grid[i][j+1] == grid[i][j + 2]:
                print(0)
                exit()
    for i in range(len(grid)):
        col = [grid[j][i] for j in range(len(grid))]
        for j in range(len(col) - 2):
            if col[j] == col[j + 1] == col[j + 2]:
                print(0)
                exit()



print(1)