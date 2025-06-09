from math import dist, floor

cx, cy, n = map(int, input().split(" "))
points = []
for i in range(n):
    x, y, r = map(int, input().split(" "))
    points.append((x, y, r))
start = 0
end = 5000
while True:
    if abs(start - end) < 0.00001:
        break
    r = (start + end)/2
    numbers_intersect = 0
    for point in points:
        distance = dist((cx, cy), (point[0], point[1]))
        if distance <= r + point[2]:
            numbers_intersect += 1
    if numbers_intersect >= 3:
        end = r
    else:
        start = r
print(floor(end))