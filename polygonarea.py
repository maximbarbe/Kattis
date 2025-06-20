while True:
    t = int(input())
    if t == 0:
        break
    points = []
    area = 0
    c = None
    for i in range(t):
        x,y = map(int, input().split())
        points.append((x, y))
    
    for i in range(t):
        area += points[i][0]*(points[(i+1)%t][1] - points[i - 1][1])
    area *= 1/2
    if area < 0:
        c = "CW"
    else:
        c = "CCW"
    area = abs(area)
    print(f"{c} {area:.1f}")