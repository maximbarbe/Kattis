n = int(input())
points = []
for i in range(n):
    ti, vi = map(float, input().split(" "))
    points.append((ti, vi))
area = 0
for i in range(len(points) - 1):
    area += ((points[i][1] + points[i + 1][1])/2) * (points[i + 1][0] - points[i][0])
print(area/1000)