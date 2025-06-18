from math import pi, dist
t = int(input())
for i in range(t):
    r, n = map(int, input().split(" "))
    points = []
    d = 0
    for j in range(n):
        x, y = map(int, input().split(" "))
        points.append((x, y))
    for j in range(len(points) - 1):
        d += dist(points[j], points[j + 1])
    d += dist(points[0], points[-1])
    if d - 2*pi*r < 0:
        print("Not possible")
    else:
        print((d - 2*pi*r)/d)