import sys
from math import inf
coordinates = []

i, j = 0, 0
for line in sys.stdin:
    coordinates.append((i, j))
    line = line.rstrip()
    match line:
        case "down":
            i += 1
        case "left":
            j -= 1
        case "right":
            j += 1
        case _:
            i -= 1
else:
    coordinates.append((i, j))
    
mini = inf

minj = inf

for i, j in coordinates:

    if i < mini:
        mini = i
    if j < minj:
        minj = j
        

updated = list(map(lambda el:(el[0] + abs(mini), el[1] + abs(minj)), coordinates))

maxi = 0
maxj = 0
for i in range(len(updated)):
    if updated[i][0] > maxi:
        maxi = updated[i][0]
    if updated[i][1] > maxj:
        maxj = updated[i][1]

grid = [[' 'for i in range(maxj + 1)]for j in range(maxi + 1)]
for i,j in updated:
    grid[i][j] = "*"
grid[updated[0][0]][updated[0][1]] = "S"
grid[updated[-1][0]][updated[-1][1]] = "E"
print("#"*(len(grid[0]) + 2))
for i in range(len(grid)):
    print(f"#{''.join(grid[i])}#")
print("#"*(len(grid[0]) + 2))