first = True
while True:
    
    n = int(input())
    if n == 0:
        break
    if not first:
        print()
    first = False
    rectangles = []
    for i in range(n):
        x1, y1, x2, y2, size= input().split(" ")
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
        rectangles.append((x1, y1, x2,y2,size))
    m = int(input())
    for i in range(m):
        x,y,size = input().split(" ")
        x, y = float(x), float(y)
        for j in range(len(rectangles)):
            x1, y1, x2, y2 = rectangles[j][:-1]
            if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                if size == rectangles[j][-1]:
                    print(f"{size} correct")
                else:
                    print(f"{size} {rectangles[j][-1]}")
                break
        else:
            print(f"{size} floor")