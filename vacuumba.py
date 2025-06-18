from math import cos, sin, radians, pi

n = int(input())
for i in range(n):
    m = int(input())
    x, y, angle = 0, 0, 90
    for i in range(m):
        ang, dist = map(float, input().split(" "))
        angle += ang
        x += dist * cos(radians(angle))
        y += dist * sin(radians(angle))
    print(f"{x} {y}")