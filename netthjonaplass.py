points = []
for i in range(int(input())):
    points.append(int(input()))
points.sort()

left = 0
for p in points:
    d = (p - left)
    left += d * 2
    print(2*d)