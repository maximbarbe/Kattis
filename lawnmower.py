# ((x1, y1), (x2, y2))
import sys
from math import inf

while True:
    data = input().split(" ")
    if data[0] == data[1] == "0" and data[2] == "0.0":
        break
    else:
        vertically = False
        horizontally = False
        width = float(data[2])/2
        hor_points = [*map(float, input().split(" "))]
        vert_points = [*map(float, input().split(" "))]
        hor_points.sort()
        vert_points.sort()
        trimmed_hor = [(-inf, 0), (75, inf)]
        trimmed_vert = [(-inf, 0), (100, inf)]
        for i in range(len(hor_points)):
            if len(trimmed_hor) == 1:
                break
            for j in range(len(trimmed_hor) - 1):
                if hor_points[i] - width <= trimmed_hor[j][1]:
                    if hor_points[i] + width >= trimmed_hor[j + 1][0]:
                        first = trimmed_hor.pop(j)
                        second = trimmed_hor.pop(j)
                        trimmed_hor.append((first[0], second[1]))
                    else:
                        first = trimmed_hor.pop(j)
                        trimmed_hor.append((first[0], hor_points[i] + width))
                    break
            else:
                trimmed_hor.append((hor_points[i] - width, hor_points[i] + width))
            trimmed_hor.sort(key=lambda el: el[0])
        if trimmed_hor[0] == (-inf, inf):
            horizontally = True
        for i in range(len(vert_points)):
            if len(trimmed_vert) == 1:
                break
            for j in range(len(trimmed_vert) - 1):
                if vert_points[i] - width <= trimmed_vert[j][1]:
                    if vert_points[i] + width >= trimmed_vert[j + 1][0]:
                        first = trimmed_vert.pop(j)
                        second = trimmed_vert.pop(j)
                        trimmed_vert.append((first[0], second[1]))
                    else:
                        first = trimmed_vert.pop(j)
                        trimmed_vert.append((first[0], vert_points[i] + width))
                    break
            else:
                trimmed_vert.append((vert_points[i] - width, vert_points[i] + width))
            trimmed_vert.sort(key=lambda el: el[0])
        if trimmed_vert[0] == (-inf, inf):
            vertically = True   
        if horizontally and vertically:
            print("YES")
        else:
            print("NO")