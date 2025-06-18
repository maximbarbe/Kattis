side, horizontal, vertical = map(int, input().split(" "))
if side - horizontal > side/2:
    horizontal = side - horizontal
if side - vertical > side/2:
    vertical = side - vertical

print(horizontal * vertical * 4)