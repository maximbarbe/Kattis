from math import dist, radians, cos, sin

n = int(input())
for i in range(n):
    startx, starty, curx, cury, angle = 0,0,0,0,0
    num_commands = int(input())
    for j in range(num_commands):
        command = input().split()
        if command[0] == "fd":
            curx += int(command[1])*cos(radians(angle))
            cury += int(command[1])*sin(radians(angle))
        elif command[0] == "lt":
            angle = (angle + int(command[1])) % 360
        elif command[0] == "rt":
            angle = (angle - int(command[1])) % 360
        else:
            curx -= int(command[1])*cos(radians(angle))
            cury -= int(command[1])*sin(radians(angle))
    print(round(dist((startx, starty), (curx, cury))))