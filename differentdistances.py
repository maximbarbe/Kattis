import sys
for line in sys.stdin:
    if line == "0\n":
        break
    else:
        x_1, y_1, x_2, y_2, p = map(float, line.split(" "))
        res = (abs(x_1 - x_2)**p + abs(y_1 - y_2)**p)**(1/p)
        print(res)