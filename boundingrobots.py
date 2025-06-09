import sys

while True:
    width, height = map(int, input().split(" "))
    if width == height == 0:
        break
    robx, roby = 0, 0
    actx, acty = 0, 0
    n = int(input())
    for i in range(n):
        data = input().split(" ")
        direction = data[0]
        move = int(data[1])
        if direction == "u":
            roby += move
            if acty + move <= height - 1:
                acty += move
            else:
                acty = height - 1
        elif direction == "d":
            roby -= move
            if acty - move >= 0:
                acty -= move
            else:
                acty = 0
        elif direction == "r":
            robx += move
            if actx + move <= width - 1:
                actx += move
            else:
                actx = width - 1
        else:
            robx -= move
            if actx - move >= 0:
                actx -= move
            else:
                actx = 0
    print(f"Robot thinks {robx} {roby}")
    print(f"Actually at {actx} {acty}")
    print()