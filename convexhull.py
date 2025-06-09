from math import inf, atan2, dist

# Implementation of the pseudo-code described here:
# https://en.wikipedia.org/wiki/Graham_scan

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3= p3
    return (x2 - x1)*(y3-y1) - (y2-y1)*(x3-x1)

def convex_hull(points):
    points = list(set(points))
    stack = []
    p0 = (inf, inf)
    for x, y in points:
        if y < p0[1]:
            p0 = (x, y)
        elif y == p0[1]:
            if x < p0[0]:
                p0 = (x, y)
    points.sort(key=lambda el: (atan2(el[1] - p0[1], el[0] - p0[0]), dist(el, p0)))


    for point in points:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)
    return stack
while True:
    n = int(input())
    if n == 0:
        break
    points =[]
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    res = convex_hull(points)
    print(len(res))
    for x, y in res:
        print(x, y)