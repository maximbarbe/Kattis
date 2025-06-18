grid = []
for i in range(3):
    grid.append(input().split(" "))

# horizontal
for i in range(3):
    if grid[i][0] == grid[i][1] == grid[i][2]:
        if grid[i][0] == "X":
            print("Johan har vunnit")
            exit()
        elif grid[i][0] == "O":
            print("Abdullah har vunnit")
            exit()
# vertical
for i in range(3):
    if grid[0][i] == grid[1][i] == grid[2][i]:
        if grid[0][i] == "X":
            print("Johan har vunnit")
            exit()
        elif grid[0][i] == "O":
            print("Abdullah har vunnit")
            exit()
#diagonal
if grid[0][0] == grid[1][1] == grid[2][2]:
    if grid[0][0] == "X":
        print("Johan har vunnit")
        exit()
    elif grid[0][0] == "O":
        print("Abdullah har vunnit")
        exit()

if grid[0][2] == grid[1][1] == grid[2][0]:
    if grid[0][2] == "X":
        print("Johan har vunnit")
        exit()
    elif grid[0][2] == "O":
        print("Abdullah har vunnit")
        exit()
print("ingen har vunnit")