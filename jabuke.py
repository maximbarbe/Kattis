def get_area(x_1, y_1, x_2, y_2, x_3, y_3):
    return abs(x_1*(y_2 - y_3) + x_2*(y_3 - y_1) + x_3*(y_1 - y_2))/2
x_1, y_1 = map(int, input().split(" "))
x_2, y_2 = map(int, input().split(" "))
x_3, y_3 = map(int, input().split(" "))


area = abs(x_1*(y_2 - y_3) + x_2*(y_3 - y_1) + x_3*(y_1 - y_2))/2
print(f"{round(area, 1)}")
res = 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split(" "))
    first = get_area(x, y, x_2, y_2, x_3, y_3)
    second = get_area(x_1, y_1,x, y, x_3, y_3)
    third = get_area(x_1, y_1, x_2, y_2, x, y)
    if first + second + third == area:
        res += 1
print(res)