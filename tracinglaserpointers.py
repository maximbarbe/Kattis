n = int(input())
intersect = []
for i in range(n):
    x,y,m, name = input().split()
    x,y,m = map(float, (x, y, m))
    if y < 0 and m > 0 or y > 0 and m < 0:
        x2 = (-y + m*x)/m
        intersect.append((x2, name))
intersect.sort(key=lambda el:el[0])

for x, name in intersect:
    print(name)
        