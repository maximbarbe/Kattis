def simulate(dest, commands):
    cur = (0, 0)
    directions = ["F", "R", "D", "L"]
    dir = "F"
    dir_idx = 0
    for command in commands:
        if command == "Forward":
            if dir == "F":
                cur = (cur[0], cur[1] + 1)
            elif dir == "R":
                cur = (cur[0] + 1, cur[1])
            elif dir == "D":
                cur = (cur[0], cur[1] - 1)
            else:
                cur = (cur[0] - 1, cur[1])
        elif command == "Right":
            dir_idx = (dir_idx + 1) % 4
            dir = directions[dir_idx]
        else:
            dir_idx = (dir_idx -1 + 4) % 4
            dir = directions[dir_idx]
    if cur == dest:
        return True
    else:
        return False



x, y = map(int, input().split(" "))
dest = (x, y)
n = int(input())
cur_pos = (0, 0)
dir = "F"
commands = []
for i in range(n):
    commands.append(input())
for i in range(n):
    temp = commands[i]
    for command in ["Forward", "Right", "Left"]:
        if command != temp:
            commands[i] = command
            if simulate(dest, commands):
                print(f"{i+1} {command}")
                exit()
    commands[i] = temp