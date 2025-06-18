x, y = map(int, input().split(" "))
if x == 0:
    if y == 1:
        print("ALL GOOD")
    else:
        print(0)
elif y == 1:
    if x != 0:
        print("Impossible")
    else:
        print("ALL GOOD")
else:
    print(-x/(y-1))