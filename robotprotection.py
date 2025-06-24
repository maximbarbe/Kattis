from math import atan2, dist
from collections import defaultdict


def cross_product(x1, y1, x2, y2):
    return x1*y2 - x2*y1


def ccw(x1, y1, x2, y2, x3, y3):
    v1 = (x2 - x1, y2 - y1)
    v2 = (x3 - x1, y3 - y1)
    return cross_product(*v1, *v2) < 0

while True:
    angles = defaultdict(lambda:[])
    n = int(input())
    if n == 0:
        break
    points = []
    for i in range(n):
        x,y = map(int, input().split())
        points.append((x, y))
    smallest_y = 10001
    pt = None
    pts = []
    for x, y in points:
        if y < smallest_y:
            smallest_y = y
            pt = (x, y)
        elif y == smallest_y:
            if x < pt[0]:
                pt = (x, y)
    for i, (x, y) in enumerate(points):
        angle = atan2(y-pt[1], x-pt[0])
        angles[angle].append((x, y))
    points = [(*max(val, key=lambda el:dist(el, pt)), key) for key,val in angles.items()]
    
    points.sort(key=lambda el:el[2])
    stack = []
    if points[0] != (*pt, 0):
        stack.append(pt)
    for x,y,_ in points:
        while len(stack) > 1 and ccw(*stack[-2], *stack[-1], x, y):
            stack.pop()
        stack.append((x, y))
    res = 0
    for i in range(len(stack)):
        x1, y1 = stack[i]
        x2, y2 = stack[(i + 1)%len(stack)]
        res += (y1 + y2)*(x1-x2)
    
    res *= 1/2
    print(abs(res))