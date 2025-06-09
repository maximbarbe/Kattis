n = int(input())
for i in range(n):
    vals = [*map(int, input().split(" "))]
    x_values = []
    y_values = []
    for i in range(1, len(vals), 2):
        x_values.append(vals[i])
        y_values.append(vals[i + 1])
    res = 0
    # Formula: https://mathworld.wolfram.com/PolygonArea.html
    for i in range(len(x_values)):
        res += (x_values[i] * y_values[(i + 1) % len(x_values)] - x_values[(i + 1) % len(x_values)] * y_values[i])
    print(res/2)