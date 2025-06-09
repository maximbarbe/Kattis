while True:
    n = int(input())
    if n == 0:
        break
    stan, ollie = 0, 0
    points = []
    for i in range(n):
        x, y = map(int, input().split(" "))
        points.append((x, y))
    linex, liney = points[len(points)//2]
    for x,y in points:
        if x > linex and y > liney:
            stan += 1
        elif x <linex and y < liney:
            stan += 1
        elif x > linex and y < liney:
            ollie += 1
        elif x < linex and y > liney:
            ollie += 1
    print(f"{stan} {ollie}")
