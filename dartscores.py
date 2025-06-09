from math import dist

n = int(input())
for i in range(n):
    m = int(input())
    radii = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
    p = 0
    res = 0
    for j in range(m):
        x,y = map(int, input().split(" "))
        distance = dist((0, 0), (x, y))
        for k in range(len(radii)):
            if distance <=radii[k]:
                res += 10 - k
                break
    print(res)