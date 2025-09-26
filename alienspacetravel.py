x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

vertical = False
if x1 == x2:
    temp = x1
    vertical = True
else:
    slope = (y2-y1)/(x2-x1)
    origin = y2 - slope * x2
    
t = int(input())
for i in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if vertical:
        if x1 == x2:
            print("NO")
        else:
            print("YES")
    else:
        if x1 == x2:
            print("YES")
        else:
            s1 = (y2 - y1)/(x2 - x1)
            o1 = y2 - s1 * x2
            if s1 == slope and origin == o1:
                print("NO")
            elif s1 == slope:
                print("NO")
            else:
                print("YES")
        
        