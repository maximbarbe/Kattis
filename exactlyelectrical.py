x_1, y_1 = map(int, input().split(" "))
x_2, y_2 = map(int, input().split(" "))
el = int(input())
if x_1 == x_2 and y_1 == y_2:
    print("Y")
    exit()
temp = el - (abs(x_1 - x_2) + abs(y_1-y_2))
if temp < 0:
    print("N")
else:
    if temp % 2 == 0:
        print("Y")
    else:
        print("N")