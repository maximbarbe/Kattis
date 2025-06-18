grid= []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx =0
start_pos = None
diamond_pos = None
for i in range(8):
    row = []
    string = input()
    for j in range(len(string)):
        if string[j] == "T":
            start_pos = (i, j)
        if string[j] == "D":
            diamond_pos = (i, j)
        row.append(string[j])
    grid.append(row)
commands = input()
for i in range(len(commands)):
    if commands[i] == "F":
        if start_pos[0] + directions[dir_idx][0] < 0 or start_pos[0] + directions[dir_idx][0] == 8 or start_pos[1] + directions[dir_idx][1] < 0 or start_pos[1] + directions[dir_idx][1] == 8 or grid[start_pos[0] + directions[dir_idx][0]][start_pos[1] + directions[dir_idx][1]] in ["I", "C"]:
            print("Bug!")
            exit()
        else:
            start_pos = (start_pos[0] + directions[dir_idx][0], start_pos[1] + directions[dir_idx][1])
    elif commands[i] == "L":
        dir_idx = (dir_idx - 1)%4
    elif commands[i] == "R":
        dir_idx = (dir_idx + 1) % 4
    else:
        if start_pos[0] + directions[dir_idx][0] < 0 or start_pos[0] + directions[dir_idx][0] == 8 or start_pos[1] + directions[dir_idx][1] < 0 or start_pos[1] + directions[dir_idx][1] == 8 or grid[start_pos[0] + directions[dir_idx][0]][start_pos[1] + directions[dir_idx][1]] != "I":
            print("Bug!")
            exit()
        else:
            grid[start_pos[0] + directions[dir_idx][0]][start_pos[1] + directions[dir_idx][1]] = "."
if start_pos == diamond_pos:
    print("Diamond!")
else:
    print("Bug!")